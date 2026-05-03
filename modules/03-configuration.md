# Configuration Manager (configManager)

Reads and writes settings to the camera's internal configuration database.
Use `{"name": "ModuleName"}` in params to target specific config tables.

---

### `configManager.getConfig`

**Purpose:** Reads a specific configuration table.

| Param | Type | Required | Description |
|---|---|---|---|
| name | string | yes | Config table name, e.g. `"Encode"`, `"Network"`, `"AlarmOut"` |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"configManager.getConfig","params":{"name":"Encode"},"id":1,"session":"<token>"}'
```

**Usage in JS (from `preview.js`):**
```javascript
s.ConfigManager.getConfig(["Encode", "EncodeEncrypt"]).done(function(a) { ... })
// Translates to: {"method":"configManager.getConfig","params":{"name":"Encode"}}
```

**Common Config Table Names:**

| Name | Description |
|---|---|
| `Encode` | Video encoding settings (resolution, bitrate, framerate) |
| `EncodeEncrypt` | Encrypted encode settings |
| `Network` | Network configuration |
| `AlarmOut` | Alarm output configuration |
| `AlarmIn` | Alarm input configuration |
| `VideoInOptions` | Video input options |
| `VideoInDayNight` | Day/Night mode settings |
| `NTP` | NTP time sync settings |
| `PPPoE` | PPPoE dial-up config (encrypted) |
| `DDNS` | Dynamic DNS config (encrypted) |
| `VPN` | VPN config (encrypted) |
| `Email` | SMTP email config (encrypted) |
| `Record` | Recording schedule settings |
| `Snap` | Snapshot settings |

> **Note:** Encrypted configs (PPPoE, DDNS, VPN, Email) must use `system.multiSec` with AES decryption.

---

### `configManager.setConfig`

**Purpose:** Saves new settings to a configuration table.

| Param | Type | Required | Description |
|---|---|---|---|
| name | string | yes | Config table name |
| table | object | yes | Full config object (get first, modify, then set) |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"configManager.setConfig","params":{"name":"AlarmOut","table":{"Mode":1}},"id":2,"session":"<token>"}'
```

**Usage in JS (from `preview.js`):**
```javascript
s.ConfigManager.getConfig("AlarmOut").done(function(a) {
    a[c].Mode = 1;                       // Modify
    s.ConfigManager.setConfig("AlarmOut", a); // Save back
})
```

---

### `configManager.getDefault`

**Purpose:** Gets the factory default values for a config table.

| Param | Type | Required | Description |
|---|---|---|---|
| name | string | yes | Config table name |

---

### `configManager.setTemporaryConfig`

**Purpose:** Sets config temporarily (reverts on reboot). Unlike `setConfig`, changes don't persist.

| Param | Type | Required | Description |
|---|---|---|---|
| name | string | yes | Config table name |
| table | object | yes | Config values |

---

### `configManager.setChannelConfig`

**Purpose:** Sets configuration for a specific video channel (NVRs).

| Param | Type | Required | Description |
|---|---|---|---|
| name | string | yes | Config table name |
| channel | int | yes | Channel number |
| table | object | yes | Config values |

---

### `configManager.restore`

**Purpose:** Factory resets the entire device.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `configManager.restoreExcept`

**Purpose:** Factory resets device but preserves specified modules.

| Param | Type | Required | Description |
|---|---|---|---|
| except | array | yes | List of module names to preserve |

---

### `configManager.saveFile`

**Purpose:** Saves a config backup file to internal storage.

| Param | Type | Required | Description |
|---|---|---|---|
| name | string | yes | Config table name |

---

### `configManager.deleteFile`

**Purpose:** Deletes an internal config backup file.

| Param | Type | Required | Description |
|---|---|---|---|
| name | string | yes | Config file name |
