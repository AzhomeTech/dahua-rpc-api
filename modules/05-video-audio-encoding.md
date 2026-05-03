# Video, Audio & Encoding

Controls video streams, audio I/O, OSD overlays, privacy masks, active deterrence, and multi-lens stitching.

---

### `encode.getCaps`

**Purpose:** Returns supported resolutions, framerates, and codecs (H264/H265/MJPEG).

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"encode.getCaps","params":{"channel":0},"id":1,"session":"<token>"}'
```

---

### `encode.getConfigCaps`

**Purpose:** Gets encoding configuration capabilities.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `encode.updateOverlayPicture`

**Purpose:** Uploads a custom watermark/logo image to be overlaid on the video stream.

| Param | Type | Required | Description |
|---|---|---|---|
| picture | base64 | yes | Base64-encoded image data |
| channel | int | no | Channel number |

---

### `encode.setMainFormat`

**Purpose:** Sets main stream encoding format.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `encode.setExtraFormat`

**Purpose:** Sets extra/sub stream encoding format.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `encode.setSnapFormat`

**Purpose:** Sets snapshot encoding format.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## devVideoInput Commands

### `devVideoInput.getCaps`

**Purpose:** Gets video sensor capabilities.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `devVideoInput.getVideoInStatus`

**Purpose:** Gets current video input status.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `devVideoInput.getCollect`

**Purpose:** Gets video collection/capture settings.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

### `devVideoInput.autoFocus`

**Purpose:** Triggers the camera's auto-focus motor.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"devVideoInput.autoFocus","params":{"channel":0},"id":1,"session":"<token>"}'
```

---

### `devVideoInput.focusRegion`

**Purpose:** Tells camera to auto-focus on a specific drawn rectangle.

| Param | Type | Required | Description |
|---|---|---|---|
| X | int | yes | X coordinate |
| Y | int | yes | Y coordinate |
| Width | int | yes | Region width |
| Height | int | yes | Region height |
| channel | int | no | Channel number |

---

### `devVideoInput.setVideoSource`

**Purpose:** Changes sensor input source.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |
| source | int|string | yes | Source identifier |

---

### `devVideoInput.adjustIris`

**Purpose:** Adjusts exposure/iris settings for the video input.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `devVideoInput.setFishEyeEPtz`

**Purpose:** Controls dewarping coordinates for Fisheye cameras.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## devVideoOutput Commands

### `devVideoOutput.enumModes`

**Purpose:** Lists available modes for physical BNC/HDMI video outputs on NVRs.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

## devAudioInput Commands

### `devAudioInput.getCaps`

**Purpose:** Gets microphone/audio input capabilities.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

## devAudioOutput Commands

### `devAudioOutput.getCaps`

**Purpose:** Gets speaker/audio output capabilities.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

### `devAudioOutput.getCollect`

**Purpose:** Checks if the camera has an audio speaker.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

## devAudioEncode Commands

### `devAudioEncode.getFormatCaps`

**Purpose:** Gets supported audio codecs (AAC, G.711, etc.).

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

## speak Commands

### `speak.startPlay`

**Purpose:** Plays an audio file out of the camera's speaker.

| Param | Type | Required | Description |
|---|---|---|---|
| file | string | yes | Audio file path/identifier |

### `speak.stopPlay`

**Purpose:** Stops audio playback.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

## OSDManager Commands

### `OSDManager.getCaps`

**Purpose:** Gets On-Screen Display capabilities (time/date text overlays).

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |

---

## PrivacyMasking Commands

### `PrivacyMasking.setPrivacyMasking`

**Purpose:** Draws black blocks over parts of the video stream.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `PrivacyMasking.getPrivacyMaskingEnable`

**Purpose:** Checks if privacy masking is enabled.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## CoaxialControlIO Commands

### `CoaxialControlIO.control`

**Purpose:** Triggers active deterrence hardware (Sirens, White Light LEDs).

| Param | Type | Required | Description |
|---|---|---|---|
| params | array | yes | Array of control objects with `Type`, `IO`, `TriggerMode` |

**Usage in JS (from `preview.js`):**
```javascript
s.CoaxialControlIO.control([{ Type: 1, IO: 2, TriggerMode: 2 }])
```

### `CoaxialControlIO.getStatus`

**Purpose:** Gets current status of coaxial control I/O.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## MultiVideo Commands

### `MultiVideo.getSpliceCaps`

**Purpose:** Configures panoramic stitching on multi-lens cameras.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## media.getStreamUri

**Purpose:** Used to request the RTSP URL for Main Stream or Sub Stream.

| Param | Type | Required | Description |
|---|---|---|---|
| channel | int | no | Channel number |
| stream | int | no | 0 = Main, 1 = Sub stream |
