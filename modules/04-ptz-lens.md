# PTZ (Pan/Tilt/Zoom) & Lens Control

Controls camera motors, presets, tours, patterns, scans, focus, iris, and peripherals (wipers, heaters, defoggers).

---

### `ptz.start`

**Purpose:** Starts continuous PTZ movement.

| Param | Type | Required | Description |
|---|---|---|---|
| code | string | yes | Direction: `"Up"`, `"Down"`, `"Left"`, `"Right"`, `"ZoomTele"`, `"ZoomWide"`, `"FocusNear"`, `"FocusFar"`, `"IrisLarge"`, `"IrisSmall"` |
| arg1 | int | yes | Speed 1 (0-7 or 0-8 depending on protocol) |
| arg2 | int | no | Speed 2 |
| arg3 | int | no | Usually 0 |
| arg4 | int | no | Usually 0 |
| channel | int | no | Channel number (default 0) |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"ptz.start","params":{"code":"Right","arg1":4,"arg2":0,"arg3":0,"arg4":0,"channel":0},"id":15,"session":"<token>"}'
```

---

### `ptz.stop`

**Purpose:** Stops current PTZ movement.

| Param | Type | Required | Description |
|---|---|---|---|
| code | string | yes | Same direction code to stop |
| arg1 | int | yes | Same speed values |
| arg2 | int | no | Same speed values |
| arg3 | int | no | Usually 0 |
| arg4 | int | no | Usually 0 |
| channel | int | no | Channel number |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"ptz.stop","params":{"code":"Right","arg1":4,"arg2":0,"arg3":0,"arg4":0,"channel":0},"id":16,"session":"<token>"}'
```

---

### `ptz.stopMove`

**Purpose:** Immediately stops all PTZ movement (alternative to `ptz.stop`).

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `ptz.isMoving`

**Purpose:** Checks if camera is currently moving.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `ptz.getStatus`

**Purpose:** Returns current X, Y, Z coordinates and motion state.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

**Response**
```json
{
  "params": {
    "status": {
      "PTZStatus": {
        "Pan": 123.4,
        "Tilt": 45.6,
        "Zoom": 1.0,
        "Moving": true
      }
    }
  },
  "result": true
}
```

---

### `ptz.moveAbsolutely`

**Purpose:** Moves camera to exact absolute coordinates.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |
| Pan | float | yes | Horizontal position (degrees) |
| Tilt | float | yes | Vertical position (degrees) |
| Zoom | float | yes | Zoom level |
| HSpeed | int | no | Horizontal speed |
| VSpeed | int | no | Vertical speed |
| ZSpeed | int | no | Zoom speed |

---

### `ptz.moveRelatively`

**Purpose:** Moves camera by a relative offset from current position.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |
| Pan | float | yes | Relative horizontal offset |
| Tilt | float | yes | Relative vertical offset |
| Zoom | float | yes | Relative zoom offset |

---

### `ptz.gotoPreset`

**Purpose:** Moves camera to a saved preset position.

| Param | Type | Required | Description |
|---|---|---|---|
| index | int | yes | Preset index number |
| channel | int | no | Channel number |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"ptz.gotoPreset","params":{"index":1},"id":1,"session":"<token>"}'
```

---

### `ptz.setPreset`

**Purpose:** Creates a preset at current position.

| Param | Type | Required | Description |
|---|---|---|---|
| index | int | yes | Preset index number |
| name | string | no | Preset name/label |
| channel | int | no | Channel number |

---

### `ptz.removePreset`

**Purpose:** Deletes a saved preset.

| Param | Type | Required | Description |
|---|---|---|---|
| index | int | yes | Preset index to delete |
| channel | int | no | Channel number |

---

### `ptz.getPresetList`

**Purpose:** Returns list of all saved presets.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `ptz.startTour`

**Purpose:** Starts a PTZ patrol/tour.

| Param | Type | Required | Description |
|---|---|---|---|
| tour | int | yes | Tour number |
| channel | int | no | Channel number |

---

### `ptz.stopTour`

**Purpose:** Stops active PTZ patrol/tour.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `ptz.setTour`

**Purpose:** Configures a tour/patrol.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `ptz.autoTour`

**Purpose:** Starts a 360-degree auto pan.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `ptz.startPatternRecord`

**Purpose:** Records manual PTZ movements as a pattern.

| Param | Type | Required | Description |
|---|---|---|---|
| index | int | yes | Pattern number |

---

### `ptz.startPatternReplay`

**Purpose:** Replays a recorded PTZ movement pattern.

| Param | Type | Required | Description |
|---|---|---|---|
| index | int | yes | Pattern number |

---

### `ptz.stopPatternReplay`

**Purpose:** Stops pattern replay.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `ptz.startScan`

**Purpose:** Starts auto-panning between two limit positions.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `ptz.stopScan`

**Purpose:** Stops auto-panning.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `ptz.setScanLimit`

**Purpose:** Sets left/right limit positions for scan.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `ptz.focusManually`

**Purpose:** Manually adjusts lens focus.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `ptz.focusRegion`

**Purpose:** Tells camera to auto-focus on a specific rectangle area.

| Param | Type | Required | Description |
|---|---|---|---|
| X | int | yes | X coordinate |
| Y | int | yes | Y coordinate |
| Width | int | yes | Width of region |
| Height | int | yes | Height of region |
| channel | int | no | Channel number |

---

### `ptz.adjustIris`

**Purpose:** Manually opens or closes the lens iris.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `ptz.auxControl`

**Purpose:** Sends raw Pelco-D auxiliary commands.

| Param | Type | Required | Description |
|---|---|---|---|
| index | int | yes | Auxiliary command index |
| channel | int | no | Channel number |

---

### `ptz.menuControl`

**Purpose:** Sends menu navigation commands (for OSD menus).

| Param | Type | Required | Description |
|---|---|---|---|
| code | string | yes | Menu command code |
| channel | int | no | Channel number |

---

### `ptz.lensInit`

**Purpose:** Recalibrates the lens motors (re-homes the lens).

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `ptz.restartPtz`

**Purpose:** Reboots the PTZ motor board without rebooting the entire camera.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `ptz.attachStatusProc`

**Purpose:** Subscribes to real-time PTZ movement status updates.

| Param | Type | Required | Description |
|---|---|---|---|
| callback | function | yes | Status update callback |

---

### `ptz.getCurrentProtocolCaps`

**Purpose:** Gets PTZ protocol capabilities for current configuration.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `ptz.gotoLimit`

**Purpose:** Moves camera to a boundary limit.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## ptzBase Commands

### `ptzBase.getHFovValue`

**Purpose:** Gets the current horizontal Field of View in degrees.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

### `ptzBase.getCurrentFovValue`

**Purpose:** Gets the current Field of View value.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

## PtzFunc Commands

### `PtzFunc.setPanGroup`

**Purpose:** Sets pan group configuration.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `PtzFunc.getPanGroup`

**Purpose:** Gets pan group configuration.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `PtzFunc.gotoPanPosition`

**Purpose:** Goes to a specific pan position.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## PtzPeripheral Commands

### `PtzPeripheral.clearFogStrongly`

**Purpose:** Triggers the optical defogger at maximum strength.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `PtzPeripheral.startClearFrost`

**Purpose:** Turns on the lens defroster heater.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `PtzPeripheral.controlPtzHeater`

**Purpose:** Sets manual heater timer.

| Param | Type | Required | Description |
|---|---|---|---|
| time | int | yes | Duration in seconds |

**Usage in JS (from `preview.js`):**
```javascript
s.PtzPeripheral.controlPtzHeater(time);
```

### `PtzPeripheral.adjustLaserAxis`

**Purpose:** Aligns the IR/Laser night vision axis.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## LensFunc Commands

### `LensFunc.autoBackFocus`

**Purpose:** Auto-adjusts back focus on Box cameras.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `LensFunc.adjustDepthField`

**Purpose:** Adjusts depth of field on advanced optics.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## RainBrush Commands

### `rainBrush.moveContinuously`

**Purpose:** Turns on the physical windshield wiper.

| Param | Type | Required | Description |
|---|---|---|---|
| speed | int | yes | Wiper speed |

**Usage in JS (from `preview.js`):**
```javascript
s.RainBrush.moveContinuously(b); // Start wiper
s.RainBrush.stopMove();          // Stop wiper
```

### `rainBrush.stopMove`

**Purpose:** Stops the wiper.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

### `rainBrush.washOnce`

**Purpose:** Triggers a single wash cycle.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |
