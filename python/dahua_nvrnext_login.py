#!/usr/bin/env python3
"""
DAHUA NVR NEXT 固件 (DHI-NVR5xxx-EI) 登入 + API 客戶端
逆向自 NVR NEXT web 固件 2026-10-27，實測 result:true。

登入公式（大寫兩步 MD5）：
  H1 = MD5("user:realm:password").UPPER
  H2 = MD5("user:random:H1").UPPER
  第二步 payload 必須帶 passwordType:"Default" + authorityType:"Default" + session

用法：
  python3 dahua_nvrnext_login.py --host http://<nvr-ip> --user <user> --password '***' --call ChannelManager.getChannelStatus
"""
import argparse
import hashlib
import json
import sys
import urllib.request


def md5u(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest().upper()


class DahuaNvrNext:
    def __init__(self, host: str, timeout: int = 10):
        self.base = host.rstrip("/")
        self.timeout = timeout
        self.session = None
        self._id = 0

    def _post(self, path: str, payload: dict) -> dict:
        data = json.dumps(payload).encode()
        req = urllib.request.Request(
            self.base + path, data=data,
            headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=self.timeout) as r:
            return json.loads(r.read())

    def _rpc(self, path: str, method: str, params=None, session=None) -> dict:
        self._id += 1
        body = {"method": method, "params": params, "id": self._id}
        sid = session or self.session
        if sid:
            body["session"] = sid
        return self._post(path, body)

    def login(self, user: str, password: str) -> str:
        # Step 1: challenge
        c = self._rpc("/RPC2_Login", "global.login",
                      {"userName": user, "password": "", "clientType": "Web3.0"})
        p = c["params"]
        realm, rnd = p["realm"], p["random"]
        h1 = md5u(f"{user}:{realm}:{password}")
        h2 = md5u(f"{user}:{rnd}:{h1}")
        # Step 2
        r = self._rpc("/RPC2_Login", "global.login", {
            "userName": user, "password": h2, "clientType": "Web3.0",
            "authorityType": "Default", "passwordType": "Default",
        }, session=c["session"])
        if not r.get("result"):
            raise RuntimeError(f"login failed: {r}")
        self.session = r["session"]
        return self.session

    def call(self, method: str, params=None) -> dict:
        return self._rpc("/RPC2", method, params)

    def keepalive(self, timeout_sec: int = 300) -> dict:
        return self.call("global.keepAlive", {"timeout": timeout_sec})

    def logout(self) -> dict:
        r = self.call("global.logout", {})
        self.session = None
        return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", required=True)
    ap.add_argument("--user", required=True)
    ap.add_argument("--password", required=True)
    ap.add_argument("--call", action="append", default=[],
                    help="RPC method to call after login (repeatable)")
    args = ap.parse_args()

    c = DahuaNvrNext(args.host)
    c.login(args.user, args.password)
    print(f"login ok, session={c.session}", file=sys.stderr)
    for m in args.call:
        r = c.call(m)
        print(json.dumps(r, ensure_ascii=False, indent=2))
    try:
        c.logout()
    except Exception:
        pass


if __name__ == "__main__":
    main()
