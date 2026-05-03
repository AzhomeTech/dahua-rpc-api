# Intelligent Video System (IVS), Analytics & Face Recognition

Configures AI rules, tripwires, intrusion detection, auto-tracking, face databases, people counting, and traffic/vehicle analytics.

---

## devVideoAnalyse Commands

### `devVideoAnalyse.getCaps`

**Purpose:** Lists supported AI modules (Tripwire, Intrusion, Abandoned Object, Missing Object, etc.).

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `devVideoAnalyse.setModuleState`

**Purpose:** Turns specific IVS rules on or off.

| Param | Type | Required | Description |
|---|---|---|---|
| module | string | yes | Module rule name |
| enable | boolean | yes | true = on, false = off |
| channel | int | no | Channel number |

---

## devVideoDetect Commands

### `devVideoDetect.attachMotionData`

**Purpose:** Subscribes to real-time motion detection grid data.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `devVideoDetect.getCaps`

**Purpose:** Gets video detection capabilities.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

## devIntelliTracker Commands

### `devIntelliTracker.trackObject`

**Purpose:** Tells a PTZ camera to lock onto and track a specific bounding box.

| Param | Type | Required | Description |
|---|---|---|---|
| X | int | yes | Bounding box X |
| Y | int | yes | Bounding box Y |
| Width | int | yes | Bounding box width |
| Height | int | yes | Bounding box height |
| channel | int | no | Channel number |

---

### `devIntelliTracker.start`

**Purpose:** Starts auto-tracking.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `devIntelliTracker.stop`

**Purpose:** Stops auto-tracking.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `devIntelliTracker.gotoScene`

**Purpose:** Moves PTZ to a saved tracking scene.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `devIntelliTracker.markScene`

**Purpose:** Saves current position as a tracking scene.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `devIntelliTracker.getCaps`

**Purpose:** Gets tracker capabilities, including scene limits.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## faceRecognitionServer Commands

### `faceRecognitionServer.createGroup`

**Purpose:** Creates a face database group (e.g., "Blacklist", "VIP", "Employees").

| Param | Type | Required | Description |
|---|---|---|---|
| name | string | yes | Group name |
| type | int | no | Group type identifier |

---

### `faceRecognitionServer.startFind`

**Purpose:** Starts searching the internal face database.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `faceRecognitionServer.doFind`

**Purpose:** Performs a face database search query.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `faceRecognitionServer.stopFind`

**Purpose:** Stops face database search.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `faceRecognitionServer.reAbstract`

**Purpose:** Re-processes face abstraction from stored face images.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `faceRecognitionServer.getGroupList`

**Purpose:** Gets list of face database groups.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## FaceFlowStat Commands

### `FaceFlowStat.getCaps`

**Purpose:** Configures people counting by face recognition.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## trafficFlowStat Commands

### `trafficFlowStat.clearStat`

**Purpose:** Resets vehicle counting statistics.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## vehiclesDistribution Commands

### `vehiclesDistribution.getRealTimeVehiclesInfoByRegion`

**Purpose:** Gets real-time traffic data for a specific road lane/region.

| Param | Type | Required | Description |
|---|---|---|---|
| region | int|string | yes | Region/lane identifier |

---

## trafficSnap Commands

### `trafficSnap.openStrobe`

**Purpose:** Triggers the high-speed strobe light for License Plate cameras (ANPR/LPR).

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |
