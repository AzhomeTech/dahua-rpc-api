# System, MagicBox & Device Info

Controls device state, time, hardware info, and process management.

---

### `system.listMethod`

**Purpose:** Returns every RPC method your firmware supports.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

**Response**
```json
{
  "id": 5,
  "params": {
    "method": ["system.listMethod", "global.login", "ptz.start", ...]
  },
  "result": true,
  "session": "<token>"
}
```

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"system.listMethod","params":null,"id":1,"session":"<token>"}'
```

---

### `system.multicall`

**Purpose:** Execute multiple RPC calls in one HTTP request.

| Param | Type | Required | Description |
|---|---|---|---|
| params | array | yes | Array of sub-request objects, each with `method`, `params`, `id` |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"system.multicall","params":[{"method":"ptz.start","params":{"code":"Right","arg1":4,"arg2":0,"arg3":0,"arg4":0,"channel":0},"id":2}],"id":4,"session":"<token>"}'
```

---

### `system.multiSec`

**Purpose:** Sends encrypted RPC calls (RSA/AES). Used for sensitive commands like user management, password changes, and encrypted configs (PPPoE, DDNS, VPN, Email).

| Param | Type | Required | Description |
|---|---|---|---|
| params | string | yes | Encrypted payload string |

> **Note:** Params must be encrypted with RSA (public key from camera via `Security.getEncryptInfo`) or AES-128/256 before sending.

---

### `global.getCurrentTime`

**Purpose:** Gets the camera's internal clock.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"global.getCurrentTime","params":null,"id":1,"session":"<token>"}'
```

---

### `global.setCurrentTime`

**Purpose:** Sets the camera's internal clock.

| Param | Type | Required | Description |
|---|---|---|---|
| time | string | yes | ISO 8601 datetime string |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"global.setCurrentTime","params":{"time":"2024-01-01T12:00:00Z"},"id":1,"session":"<token>"}'
```

---

### `magicBox.reboot`

**Purpose:** Reboots the camera.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"magicBox.reboot","params":null,"id":1,"session":"<token>"}'
```

---

### `magicBox.needReboot`

**Purpose:** Checks if a restart is pending (e.g. after config change).

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `magicBox.shutdown`

**Purpose:** Turns the device off (not just reboot).

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `magicBox.resetSystem`

**Purpose:** Reboots the camera (requires password in params). Alternative to `magicBox.reboot`.

| Param | Type | Required | Description |
|---|---|---|---|
| password | string | yes | Hashed admin password |

---

### `magicBox.getSerialNo`

**Purpose:** Returns the device serial number.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"magicBox.getSerialNo","params":null,"id":1,"session":"<token>"}'
```

---

### `magicBox.getDeviceType`

**Purpose:** Returns device type identifier (e.g. "IPC", "SD", "NVR").

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `magicBox.getDeviceClass`

**Purpose:** Returns device class.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `magicBox.getHardwareType`

**[Params TBD — truncated in source. See `system.listMethod` output for your firmware.]**

---

### `magicBox.getSoftwareVersion`

**Purpose:** Returns current firmware version string.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"magicBox.getSoftwareVersion","params":null,"id":1,"session":"<token>"}'
```

---

### `magicBox.getHardwareVersion`

**Purpose:** Returns hardware version string.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `magicBox.getSystemInfo`

**Purpose:** Retrieves serial number, hardware model, device type.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"magicBox.getSystemInfo","params":null,"id":12,"session":"<token>"}'
```

**Response**
```json
{
  "id": 12,
  "params": {
    "appAutoStart": true,
    "deviceType": "IPC",
    "hardwareVersion": "1.0.0",
    "serialNumber": "AMC123456789"
  },
  "result": true,
  "session": "<token>"
}
```

---

### `magicBox.getOSInfo`

**Purpose:** Gets the OS type running on the camera.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `magicBox.getMemoryInfo`

**Purpose:** Returns RAM usage statistics.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `magicBox.getCPUUsage`

**Purpose:** Returns CPU load percentage.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `magicBox.getUpTime`

**Purpose:** Returns system uptime since last reboot.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `magicBox.getProcessInfo`

**Purpose:** Returns list of running services/daemons.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `magicBox.getSubModules`

**Purpose:** Returns sub-module status information.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `magicBox.getMarketArea`

**Purpose:** Returns the device's market region code.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `CameraModule.getSerialNo`

**Purpose:** Gets hardware serial number (alternative to `magicBox.getSerialNo`).

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `DevInit.getStatus`

**Purpose:** Used during first-time setup wizard. Gets device initialization status.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `DevInit.account`

**Purpose:** First-time setup: creates initial admin account with encrypted params.

| Param | Type | Required | Description |
|---|---|---|---|
| salt | string | yes | Salt value |
| cipher | string | yes | Encryption cipher |
| content | string | yes | Encrypted account content |

> **Note:** Uses encrypted params via `system.multiSec`.

---

### `DevInit.access`

**Purpose:** First-time setup: configures access control.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `WebInit.getCaps`

**Purpose:** Gets capabilities of the web server interface.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |
