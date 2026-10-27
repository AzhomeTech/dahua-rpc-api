# Dahua IP Camera / NVR JSON-RPC API Reference

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Methods](https://img.shields.io/badge/methods-275%2B-blue.svg)](https://github.com/H3xano/dahua-rpc-api)

Exhaustive documentation of the Dahua proprietary JSON-RPC API, reverse-engineered from the device's internal JavaScript source files (`rpc.js`, `rpcBase.js`, `rpcLogin.js`).

## Architecture

Dahua devices use a proprietary **JSON-RPC 2.0 over HTTP** protocol.

| Property | Value |
|---|---|
| HTTP Method | `POST` |
| Content-Type | `application/json` |
| Auth Endpoint | `/RPC2_Login` |
| Command Endpoint | `/RPC2` |
| Unauthenticated Endpoint | `/OutsideCmd` (password reset, etc.) |

### Standard Payload Structure

Every request follows this exact JSON structure (from `rpcBase.js`):

```json
{
  "method": "moduleName.actionName",
  "params": { "key": "value" },
  "id": 1,
  "session": "YOUR_SESSION_ID"
}
```

| Field | Description |
|---|---|
| `method` | The action to perform, e.g. `ptz.start` |
| `params` | Arguments object. Send `null` if none. |
| `id` | Integer, increment by 1 per request |
| `session` | Session token from login |

### Endpoints

| Endpoint | Purpose |
|---|---|
| `/RPC2_Login` | Authentication only (`global.login`) |
| `/RPC2` | All standard RPC commands |
| `/OutsideCmd` | Unauthenticated commands (password reset) |

---

## Authentication (2-Step Challenge-Response Handshake)

Dahua never sends passwords in plain text. Uses a challenge-response mechanism from `rpcLogin.js`.

### Step 1: The Challenge

Send login with **empty** password to `/RPC2_Login`:

```json
{
  "method": "global.login",
  "params": { "userName": "admin", "password": "", "clientType": "Web3.0" },
  "id": 1
}
```

**Response:** Camera returns error `Code 268632079` but includes critical tokens in `params`:
- `realm` — e.g. "Login to 4X02345PAJ9A82F"
- `random` — random string for this session
- `session` — temporary session ID

### Step 2: The Response

Hash password locally using the formula from `k.getAuth` in `rpcLogin.js`:

```
Hash1 = MD5(username + ":" + realm + ":" + plain_password)
Hash2 = MD5(username + ":" + random + ":" + Hash1)
```

Send second request to `/RPC2_Login` with `Hash2` as password and the temporary `session`:

```json
{
  "method": "global.login",
  "params": { "userName": "admin", "password": "<Hash2>", "clientType": "Web3.0" },
  "id": 2,
  "session": "<temporary_session>"
}
```

**Success response:** `{"result": true, "session": "<permanent_session>"}`

### Encryption Modes

| Mode | Formula | Source |
|---|---|---|
| Basic | `Base64(username + ":" + password)` | `rpcLogin.js` |
| Default | `MD5(user:random:MD5(user:realm:pass))` | `rpcLogin.js` |

---

## Special Mechanisms

### Multicall (Batching)

Execute multiple commands in one HTTP request with `system.multicall`:

```json
{
  "method": "system.multicall",
  "params": [
    {"method": "ptz.start", "params": {"code": "Right", "arg1": 4, "arg2": 0, "arg3": 0, "arg4": 0, "channel": 0}, "id": 2},
    {"method": "ptz.stop", "params": {"code": "Right", "arg1": 4, "arg2": 0, "arg3": 0, "arg4": 0, "channel": 0}, "id": 3}
  ],
  "id": 4,
  "session": "<token>"
}
```

### Secure Calls (`system.multiSec`)

Sensitive commands (adding users, modifying passwords, network configs like PPPoE/VPN/DDNS/Email) use `system.multiSec`. The UI encrypts `params` with RSA (public key from camera) or AES-128/256 before sending.

### Discovery Command

`system.listMethod` returns every RPC method your firmware supports:

```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"system.listMethod","params":null,"id":1,"session":"<token>"}'
```

---

## Session Lifecycle

- Send `global.keepAlive` every ~60 seconds to prevent session expiry
- Session invalid = error code `287637504`
- On invalidation, the UI auto-reconnects via `rpcLogin.js` keepalive handler
- After 5 consecutive keepalive failures, the UI reloads

---

## Best Practices

1. **Check abilities first:** The UI uses `jsCore/ability.js` to ask camera if it supports a feature before showing buttons. Don't assume a command works (e.g. `ptz.start` fails on static dome).
2. **Keep-alive:** Sessions expire if idle. Send `global.keepAlive` every ~60 seconds.
3. **Encrypted configs:** NVRs and newer IPCs encrypt network configs. `configManager.getConfig` for `"PPPoE"`, `"DDNS"`, `"VPN"`, `"Email"` requires `system.multiSec` with AES. Basic settings (Video encode, etc.) work with standard RPC.

---

## Module Reference

| Module | File |
|---|---|
| Core Endpoints & Payload | `modules/00-core-endpoints.md` |
| Authentication & Session | `modules/01-authentication.md` |
| System & MagicBox | `modules/02-system-magicbox.md` |
| Configuration Manager | `modules/03-configuration.md` |
| PTZ & Lens Control | `modules/04-ptz-lens.md` |
| Video, Audio & Encoding | `modules/05-video-audio-encoding.md` |
| Alarms & Events | `modules/06-alarms-events.md` |
| IVS, Analytics & Faces | `modules/07-ivs-analytics-faces.md` |
| Storage & Files | `modules/08-storage-files.md` |
| Network & Connectivity | `modules/09-network.md` |
| Security & Users | `modules/10-security-users.md` |
| Thermography & Sensors | `modules/11-thermography-sensors.md` |
| Maintenance & Upgrades | `modules/12-maintenance-upgrade.md` |

## Python Client

See `reference/dahua_rpc_client.py` for a working Python login + discovery script.

---

## Fork 備註 (AzhomeTech)

呢個 fork 加入咗 **NVR NEXT 新版固件** (DHI-NVR5232-EI, 2026-10-27 逆向) 嘅實測筆記：

- [`NVR-NEXT-FIRMWARE-NOTES.md`](NVR-NEXT-FIRMWARE-NOTES.md) — 大寫兩步 MD5 登入公式、錯誤碼語義、260 服務清單、新舊方法名對照
- [`python/dahua_nvrnext_login.py`](python/dahua_nvrnext_login.py) — 可直接運行嘅登入客戶端

原 repo 嘅小寫 MD5 公式喺新版固件會回 `268632085 User or password not valid`；用大寫版即通。
