# Authentication & Session Management

All auth commands source from `rpcLogin.js` and `rpcBase.js`.

---

### `global.login`

**Purpose:** Authenticate user via 2-step challenge-response handshake.

**Step 1 — Challenge Request**

| Param | Type | Required | Description |
|---|---|---|---|
| userName | string | yes | Username (e.g. "admin") |
| password | string | yes | **Empty string** for step 1 |
| clientType | string | yes | `"Web3.0"` |
| loginType | string | no | `"Direct"`, `"LDAP"`, `"ActiveDirectory"` |
| authorityType | string | no | `"Default"` |

**cURL (Step 1: /RPC2_Login)**
```bash
curl -X POST http://<camera-ip>/RPC2_Login \
  -H "Content-Type: application/json" \
  -d '{"method":"global.login","params":{"userName":"admin","password":"","clientType":"Web3.0"},"id":1}'
```

**Response (on challenge):**
```json
{
  "id": 1,
  "error": { "code": 268632079 },
  "params": {
    "realm": "Login to 4X02345PAJ9A82F",
    "random": "123456789"
  },
  "result": false,
  "session": "abc123temp"
}
```

**Step 2 — Authentication Request**

| Param | Type | Required | Description |
|---|---|---|---|
| userName | string | yes | Username |
| password | string | yes | Hashed password (see formula below) |
| clientType | string | yes | `"Web3.0"` |
| loginType | string | no | `"Direct"`, `"LDAP"`, `"ActiveDirectory"` |
| authorityType | string | no | `"Default"` |

Must include `session` from step 1 response.

**cURL (Step 2: /RPC2_Login)**
```bash
curl -X POST http://<camera-ip>/RPC2_Login \
  -H "Content-Type: application/json" \
  -d '{"method":"global.login","params":{"userName":"admin","password":"<hash2>","clientType":"Web3.0"},"id":2,"session":"abc123temp"}'
```

**Success Response:**
```json
{
  "id": 2,
  "params": null,
  "result": true,
  "session": "def456permanent"
}
```

**Hashing Formula (from `rpcLogin.js` `k.getAuth`)**

```
Default mode: MD5(username + ":" + random + ":" + MD5(username + ":" + realm + ":" + password))
Basic mode:   Base64(username + ":" + password)
```

> **Note:** After login, `rpcLogin.js` calls `UserManager.getUserInfo(username)` or `UserManager.getAuthorityList()` to load user permissions.

---

### `global.keepAlive`

**Purpose:** Prevents session timeout. Send every ~60 seconds.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params required |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"global.keepAlive","params":null,"id":10,"session":"<token>"}'
```

**KeepAlive Retry Logic (from `rpcLogin.js`):**
- On success → reset fail counter to 0
- On error code `287637504` → clear interval (session dead)
- On 5 consecutive failures → alert user, reload page
- If Ushield available → re-authenticate via hardware token

---

### `global.logout`

**Purpose:** Terminates the current session.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params required |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"global.logout","params":null,"id":11,"session":"<token>"}'
```

---

### Authority Types (from `rpcLogin.js` `k.chkAuthority`)

| Authority Key | Permission |
|---|---|
| `AuthManuCtr` | PTZ Control |
| `AuthEventCfg` | Alarm & IVS settings |
| `AuthStoreCfg` | SD Card / Recording settings |
| `AuthPeripheral` | Wiper, Heater, White Light |
| `AuthSysCfg` | General system configuration |
| `AuthNetCfg` | Network configuration |
| `AuthVideoCfg` | Video & Encode settings |
| `AuthAccount` | User account management |
| `AuthFileQuery` | File / recording query |
| `AuthLogQuery` | Log query |
| `AuthAbnormal` | System abnormal events |
| `AuthTalk` | Two-way audio talk |
| `AuthBackup` | Backup & restore |
