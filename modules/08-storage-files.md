# Storage, SD Cards & File Management

Manages local storage (SD cards, HDDs), recording, snapshots, media file search, and file operations.

---

### `storage.getDeviceAllInfo`

**Purpose:** Gets SD card/HDD status, total capacity, and free space.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"storage.getDeviceAllInfo","params":null,"id":1,"session":"<token>"}'
```

---

## devStorage Commands

### `devStorage.formatPatition`

**Purpose:** Erases and formats the SD card / storage partition.

| Param | Type | Required | Description |
|---|---|---|---|
| device | string | yes | Device identifier |
| type | string | yes | Partition type |
| format | string | no | Format type |

**Usage in JS (from `rpc.js`):**
```javascript
e.DevStorage.formatPatition(b, c, d).always(function() {
    e.RecordManager.start();
    e.SnapManager.start();
})
```

> **Note:** After formatting, the UI restarts recording and snapshot services automatically.

---

## recordManager Commands

### `recordManager.start`

**Purpose:** Manually starts local video recording to SD card/HDD.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `recordManager.stop`

**Purpose:** Manually stops local video recording.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

## snapManager Commands

### `snapManager.start`

**Purpose:** Takes a snapshot and saves it to the SD card.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `snapManager.stop`

**Purpose:** Stops snapshot capture.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

## FileManager Commands

### `FileManager.list`

**Purpose:** Lists files stored on the SD card/NAS.

| Param | Type | Required | Description |
|---|---|---|---|
| path | string | yes | Directory path |

---

### `FileManager.removeFiles`

**Purpose:** Deletes files from storage.

| Param | Type | Required | Description |
|---|---|---|---|
| files | array | yes | Array of file paths to delete |

---

### `FileManager.rename`

**Purpose:** Renames a file on storage.

| Param | Type | Required | Description |
|---|---|---|---|
| oldPath | string | yes | Current file path |
| newPath | string | yes | New file path |

---

## mediaFileFind Commands

### `mediaFileFind.factory.create`

**Purpose:** Creates a finder session for searching media files.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `mediaFileFind.findFile`

**Purpose:** Searches for recorded videos by date/time criteria.

| Param | Type | Required | Description |
|---|---|---|---|
| finderToken | string | yes | Finder session token |
| startTime | string | yes | Start datetime |
| endTime | string | yes | End datetime |
| channel | int | no | Channel number |
| event | string | no | Event type filter |

---

### `mediaFileFind.findNextFile`

**Purpose:** Gets next file in search results.

| Param | Type | Required | Description |
|---|---|---|---|
| finderToken | string | yes | Finder session token |

---

### `mediaFileFind.destroy`

**Purpose:** Destroys finder session.

| Param | Type | Required | Description |
|---|---|---|---|
| finderToken | string | yes | Finder session token |

---

## RecordFinder Commands

### `RecordFinder.factory.create`

**Purpose:** Creates a recording finder for playback file search.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## RecordUpdater Commands

### `RecordUpdater.importFile`

**Purpose:** Imports a video file to the device via network.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `RecordUpdater.exportFile`

**Purpose:** Exports a video file from the device via network.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `RecordUpdater.getFileImportState`

**Purpose:** Gets the state of an ongoing file import operation.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## SDEncrypt Commands

### `SDEncrypt.encrypt`

**Purpose:** Encrypts data on the SD card.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |
