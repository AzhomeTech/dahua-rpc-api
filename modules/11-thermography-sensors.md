# Thermography, Radar & IoT Sensors

Commands for Thermal imaging cameras, Laser Rangefinders, UWB Radar, RFID readers, external sensors, gyroscopes, flash lamps, and peripheral chips.

---

## RadiometryManager Commands

### `RadiometryManager.getTemper`

**Purpose:** Gets the current temperature reading.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `RadiometryManager.getRandomPointTemper`

**Purpose:** Gets temperature at a specific X/Y coordinate in the thermal image.

| Param | Type | Required | Description |
|---|---|---|---|
| X | int | yes | X coordinate |
| Y | int | yes | Y coordinate |
| channel | int | no | Channel number |

---

### `RadiometryManager.getDistTemper`

**Purpose:** Gets temperature corrected for distance.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `RadiometryManager.getMaxTemper`

**Purpose:** Gets maximum temperature in the frame.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## ThermographyManager Commands

### `ThermographyManager.doFFC`

**Purpose:** Triggers a Flat Field Correction (shutter click calibration). Recalibrates the thermal sensor.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `ThermographyManager.getCaps`

**Purpose:** Gets thermography capabilities.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ThermographyManager.getExternSystemInfo`

**Purpose:** Gets external system info for thermography.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ThermographyManager.getShutterSwitchTimes`

**Purpose:** Gets shutter calibration switch count.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ThermographyManager.getDescript`

**Purpose:** Gets thermography module description.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ThermographyManager.getThermalBalance`

**Purpose:** Gets thermal balance state.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## ThermographyNuc Commands

### `ThermographyNuc.getLensInfo`

**Purpose:** Gets NUC (Non-Uniformity Correction) lens information.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ThermographyNuc.setLensId`

**Purpose:** Sets lens identifier for NUC calibration.

| Param | Type | Required | Description |
|---|---|---|---|
| lensId | string|int | yes | Lens identifier |

### `ThermographyNuc.start`

**Purpose:** Starts NUC calibration process.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ThermographyNuc.abort`

**Purpose:** Aborts NUC calibration.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ThermographyNuc.captureGain`

**Purpose:** Captures gain map.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ThermographyNuc.saveGainMap`

**Purpose:** Saves gain map to device.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ThermographyNuc.restorePrepare`

**Purpose:** Prepares for gain map restore.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ThermographyNuc.setGainMap`

**Purpose:** Sets/applies gain map.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ThermographyNuc.getGainMap`

**Purpose:** Gets current gain map.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ThermographyNuc.getCaps`

**Purpose:** Gets NUC capabilities.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## LaserDistMeasure Commands

### `LaserDistMeasure.getDistance`

**Purpose:** Gets the distance (in meters) measured by the laser rangefinder.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `LaserDistMeasure.getDistanceRes`

**Purpose:** Gets distance measurement resolution.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `LaserDistMeasure.getCaps`

**Purpose:** Gets laser distance measurement capabilities.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `LaserDistMeasure.displayDistanceOnOSD`

**Purpose:** Displays laser distance on OSD overlay.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## TemperCorrection Commands

### `TemperCorrection.adjustBlkBdyDist`

**Purpose:** Calibrates thermal camera using a Blackbody reference at a known distance.

| Param | Type | Required | Description |
|---|---|---|---|
| distance | float | yes | Distance to blackbody |
| temperature | float | yes | Blackbody temperature |

---

### `TemperCorrection.getNucInfo`

**Purpose:** Gets NUC correction information.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `TemperCorrection.setNucInfo`

**Purpose:** Sets NUC correction information.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## FlirDebug Commands

### `FlirDebug.getSensorSetting`

**Purpose:** Advanced debugging for FLIR thermal sensor cores.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## ThermoRefrigerate Commands

### `ThermoRefrigerate.controlSensor`

**Purpose:** Controls thermal sensor cooling/refrigeration.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## UWB Commands

### `UWB.recvMsg`

**Purpose:** Receives messages from Ultra-Wideband Radar modules.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `UWB.sendMsg`

**Purpose:** Sends messages to UWB Radar modules.

| Param | Type | Required | Description |
|---|---|---|---|
| msg | string|object | yes | Message to send |

---

## RfidManager Commands

### `RfidManager.getSignalThreshold`

**Purpose:** Gets RFID reader signal threshold.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `RfidManager.setSignalThreshold`

**Purpose:** Sets RFID reader signal threshold.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `RfidManager.getVersion`

**Purpose:** Gets RFID manager version.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `RfidManager.getReceiverID`

**Purpose:** Gets RFID receiver ID.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## ExternalSensorManager Commands

### `ExternalSensorManager.getCaps`

**Purpose:** Gets external sensor capabilities.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `ExternalSensorManager.startFind`

**Purpose:** Communicates with external serial sensors (e.g. weather stations).

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## PeripheralChip Commands

### `PeripheralChip.getCaps`

**Purpose:** Gets peripheral chip capabilities.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `PeripheralChip.getVersion`

**Purpose:** Gets peripheral chip firmware version.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## Gyro Commands

### `Gyro.getData`

**Purpose:** Gets gyroscope/accelerometer data (image stabilization).

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## devFlashLampManager Commands

### `devFlashLampManager.getCaps`

**Purpose:** Gets flash lamp/strobe capabilities.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |
