# Network & Connectivity

Manages IP configuration, WiFi, DDNS, UPnP, PPPoE, and wireless connectivity (LoRa, Mobile).

---

### `netApp.getNetInterfaces`

**Purpose:** Gets all network interface details: IP address, subnet mask, gateway, MAC address.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

**cURL**
```bash
curl -X POST http://<camera-ip>/RPC2 \
  -H "Content-Type: application/json" \
  -d '{"method":"netApp.getNetInterfaces","params":null,"id":1,"session":"<token>"}'
```

---

### `netApp.getUPnPStatus`

**Purpose:** Checks if UPnP port forwarding is active.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `netApp.connectByWps`

**Purpose:** Connects the camera to a WiFi router via WPS.

| Param | Type | Required | Description |
|---|---|---|---|
| mode | string | no | WPS mode (PBC/PIN) |
| pin | string | no | PIN if PIN mode |

---

### `netApp.sendTestMail`

**Purpose:** Tests the SMTP email configuration by sending a test email.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `netApp.checkIPConflict`

**Purpose:** Pings an IP address to check if it's already in use on the network.

| Param | Type | Required | Description |
|---|---|---|---|
| ip | string | yes | IP address to check |

---

### `netApp.getMobileRSSI`

**Purpose:** Gets mobile/cellular signal strength.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `netApp.getStreamUri`

**Purpose:** Gets streaming URI information.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `netApp.getCommPort`

**Purpose:** Gets communication port configuration.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## WlanManager Commands

### `WlanManager.getSTAInfo`

**Purpose:** Gets WiFi SSID, signal strength (RSSI), bandwidth, and connection status.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

## ddnsClient Commands

### `ddnsClient.getStatus`

**Purpose:** Gets Dahua/No-IP Dynamic DNS status.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

### `ddnsClient.testHostName`

**Purpose:** Tests DDNS hostname resolution.

| Param | Type | Required | Description |
|---|---|---|---|
| hostname | string | yes | Hostname to test |

---

## UPnPPortmap Commands

### `UPnPPortmap.getUPnPStatus`

**Purpose:** Checks if port forwarding via UPnP was successful.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

## PppoeCli Commands

### `PppoeCli.getPPPoEDialInfo`

**Purpose:** Gets PPPoE dial-up connection info/credentials (encrypted).

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

> **Note:** PPPoE config is encrypted. Use `system.multiSec` to read/write.

---

## WireLessLora Commands

### `WireLessLora.getConnectstatus`

**Purpose:** Checks LoRaWAN wireless connection status (for IoT-enabled cameras).

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

## mobile Commands

### `mobile.getStatus`

**Purpose:** Gets mobile network connection status.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## IntervideoClient Commands

### `IntervideoClient.test`

**Purpose:** Tests intervideo client connectivity.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## FTP Commands

### `FTP.test`

**Purpose:** Tests FTP server connectivity.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |
