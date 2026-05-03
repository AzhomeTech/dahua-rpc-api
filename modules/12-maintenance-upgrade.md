# Maintenance, Logs & Firmware Upgrades

Manages system logs, firmware upgrades (local, cloud, remote), configuration backups, plugin installation, and licenses.

---

## Log Commands

### `Log.startFind`

**Purpose:** Initiates a log search session.

| Param | Type | Required | Description |
|---|---|---|---|
| query | object | yes | Search criteria (type, time range, etc.) |

**Usage in JS (from `rpc.js`):**
```javascript
e.Log.startFind(b).then(function(b) {
    d.token = b;
    e.Log.getCount(d.token);
})
```

---

### `Log.doSeekFind`

**Purpose:** Seeks to a position in log results.

| Param | Type | Required | Description |
|---|---|---|---|
| token | string | yes | Session token |
| start | int | yes | Start position |
| count | int | yes | Number of entries to fetch |

---

### `Log.getCount`

**Purpose:** Gets the total count of matching log entries.

| Param | Type | Required | Description |
|---|---|---|---|
| token | string | yes | Session token |

---

### `Log.stopFind`

**Purpose:** Stops and cleans up a log search session.

| Param | Type | Required | Description |
|---|---|---|---|
| token | string | yes | Session token |

---

### `Log.clear`

**Purpose:** Clears all system logs.

| Param | Type | Required | Description |
|---|---|---|---|
| type | string | yes | Log type to clear |

---

### `Log.append`

**Purpose:** Appends to the log.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## upgrader Commands

### `upgrader.start`

**Purpose:** Initiates a local firmware upgrade.

| Param | Type | Required | Description |
|---|---|---|---|
| file | string | yes | Firmware file path |
| password | string | no | Admin password (if required) |

---

### `upgrader.getState`

**Purpose:** Gets current upgrade process state.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

## CloudUpgrader Commands

### `CloudUpgrader.getAutoCheck`

**Purpose:** Gets auto-check settings for OTA updates.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `CloudUpgrader.setAutoCheck`

**Purpose:** Configures automatic OTA update checking.

| Param | Type | Required | Description |
|---|---|---|---|
| enable | boolean | yes | Enable/disable auto check |
| interval | string|int | no | Check interval |

---

### `CloudUpgrader.check`

**Purpose:** Checks Dahua servers for available OTA firmware updates.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `CloudUpgrader.execute`

**Purpose:** Executes a cloud/OTA firmware upgrade.

| Param | Type | Required | Description |
|---|---|---|---|
| version | string | yes | Target firmware version |

---

## RemoteUpgrader Commands

### `RemoteUpgrader.selectDevice`

**Purpose:** Selects device(s) for remote upgrade.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `RemoteUpgrader.checkState`

**Purpose:** Checks remote upgrade state.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `RemoteUpgrader.cancel`

**Purpose:** Cancels a remote firmware upgrade.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## Backup Commands

### `Backup.manualStart`

**Purpose:** Manually backs up camera configuration to a file.

| Param | Type | Required | Description |
|---|---|---|---|
| destination | string | yes | Backup destination path |

---

### `Backup.checkCondition`

**Purpose:** Checks if backup conditions are met (space, permissions).

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `Backup.start`

**Purpose:** Starts configuration backup process.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `Backup.stop`

**Purpose:** Stops backup process.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## installManager Commands

### `installManager.start`

**Purpose:** Installs a custom `.app` plugin to the camera OS.

| Param | Type | Required | Description |
|---|---|---|---|
| package | string | yes | Plugin package path |

---

### `installManager.stop`

**Purpose:** Stops plugin installation.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `installManager.remove`

**Purpose:** Removes an installed plugin.

| Param | Type | Required | Description |
|---|---|---|---|
| package | string | yes | Plugin identifier |

### `installManager.checkState`

**Purpose:** Checks plugin installation state.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `installManager.getInstallProcessInfo`

**Purpose:** Gets detailed installation process information.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## License Commands

### `License.getLicenseInfo`

**Purpose:** Gets device license information (AI modules, channel count, etc.).

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

## workDirectory Commands

### `workDirectory.getInfo`

**Purpose:** Gets work directory information (paths, space).

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## Integration Commands (from `rpc.js`)

### `Integration.getLogCount`

**Purpose:** Gets log count via integration wrapper.

| Param | Type | Required | Description |
|---|---|---|---|
| type | string | yes | Log type |

### `Integration.getLog`

**Purpose:** Gets log entries via integration wrapper.

| Param | Type | Required | Description |
|---|---|---|---|
| token | string | yes | Session token |
| start | int | yes | Start position |
| count | int | yes | Number of entries |

### `Integration.formatPatition`

**Purpose:** Formats storage partition and auto-restarts recording/snapshot services.

| Param | Type | Required | Description |
|---|---|---|---|
| device | string | yes | Device identifier |
| type | string | yes | Partition type |
| format | string | no | Format type |
