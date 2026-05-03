# Alarms & Event Management

Subscribes to and triggers events. Manages physical alarm I/O ports and PIR sensors.

---

### `alarm.getInSlots`

**Purpose:** Gets the number of physical alarm input wiring ports.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `alarm.getOutSlots`

**Purpose:** Gets the number of physical alarm output wiring ports.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `alarm.getOutState`

**Purpose:** Reads the current state of alarm outputs.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel/index |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"alarm.getOutState","params":{"channel":0},"id":1,"session":"<token>"}'
```

---

### `alarm.getAlarmCaps`

**Purpose:** Gets alarm capabilities.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## PirAlarm Commands

### `PirAlarm.getParam`

**Purpose:** Gets PIR (Passive Infrared) motion sensor parameters.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `PirAlarm.setParam`

**Purpose:** Configures PIR motion sensor.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## eventManager Commands

### `eventManager.attach`

**Purpose:** Subscribes to real-time event streams (motion detection, IVS events, etc.).

| Param | Type | Required | Description |
|---|---|---|---|
| codes | array | yes | List of event codes to subscribe to |
| callback | function | yes | Event handler callback |

**Usage in JS (from `rpc.js`):**
```javascript
eventManager.attach(["VideoMotion", "VideoLoss"], function(event) { ... })
```

### `eventManager.detach`

**Purpose:** Unsubscribes from event streams.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `eventManager.destroy`

**Purpose:** Destroys event manager instance.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `eventManager.getEventData`

**Purpose:** Retrieves data about a specific past event.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `eventManager.confirmEvent`

**Purpose:** Acknowledges/confirms an alarm event.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `eventManager.getEventList`

**Purpose:** Gets list of recent events.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## Event Codes (Common)

| Code | Description |
|---|---|
| `VideoMotion` | Motion detection |
| `VideoLoss` | Video signal loss |
| `VideoBlind` | Video tampering/blinding |
| `AlarmLocal` | Local alarm input trigger |
| `AlarmOutOpen` | Alarm output opened |
| `AlarmOutClose` | Alarm output closed |
| `AlarmNet` | Network alarm |
| `StorageNotExist` | No storage device |
| `StorageFailure` | Storage failure |
| `StorageLowSpace` | Low storage space |
| `IntelliEvent` | IVS/Analytics event |
| `FaceDetection` | Face detected |
| `CrossLineDetection` | Tripwire crossed |
| `CrossRegionDetection` | Intrusion detected |
| `AbandonedObject` | Abandoned object detected |
| `MissingObject` | Missing object detected |
| `TemperatureAlarm` | Thermal temperature alarm |
| `FireWarning` | Fire/smoke detected |
