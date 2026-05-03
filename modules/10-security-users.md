# Security, Users & Certificates

Manages authentication, user accounts, password recovery, digital certificates, and encrypted video standards.

---

## userManager Commands

### `userManager.getUserInfoAll`

**Purpose:** Lists all users on the device.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `userManager.getUserInfo`

**Purpose:** Gets info for a specific user (called after login by `rpcLogin.js`).

| Param | Type | Required | Description |
|---|---|---|---|
| name | string | yes | Username |

---

### `userManager.addUser`

**Purpose:** Creates a new user account.

| Param | Type | Required | Description |
|---|---|---|---|
| user | object | yes | User object (name, password hash, group, authorityList, etc.) |

> **Note:** Often uses `system.multiSec` for encrypted password transmission.

---

### `userManager.deleteUser`

**Purpose:** Deletes a user account.

| Param | Type | Required | Description |
|---|---|---|---|
| name | string | yes | Username to delete |

---

### `userManager.modifyUser`

**Purpose:** Modifies user account settings (group, permissions, etc.).

| Param | Type | Required | Description |
|---|---|---|---|
| user | object | yes | Modified user object |

---

### `userManager.modifyPassword`

**Purpose:** Changes a user's password (requires old password hash).

| Param | Type | Required | Description |
|---|---|---|---|
| name | string | yes | Username |
| oldPwd | string | yes | Hashed old password |
| newPwd | string | yes | Hashed new password |

**Usage in JS (from `index.js`):**
```javascript
y.UserManager.modifyPassword(username, old_hash, new_hash)
```

> **Note:** Dahua hashes passwords with MD5 before sending via RPC. Uses `hex_md5()`.

---

### `userManager.getAuthorityList`

**Purpose:** Gets the full permission matrix (all available authority types on the device).

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

**Called after login (from `rpcLogin.js`):**
```javascript
h.UserManager.getAuthorityList().done(function(a) {
    m.AuthorityList = a
})
```

---

### `userManager.getGroupInfoAll`

**Purpose:** Lists all user groups.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### `userManager.addGroup`

**Purpose:** Creates a new user group.

| Param | Type | Required | Description |
|---|---|---|---|
| group | object | yes | Group object |

---

### `userManager.deleteGroup`

**Purpose:** Deletes a user group.

| Param | Type | Required | Description |
|---|---|---|---|
| name | string | yes | Group name |

---

### `userManager.modifyGroup`

**Purpose:** Modifies a user group.

| Param | Type | Required | Description |
|---|---|---|---|
| group | object | yes | Modified group object |

---

### `userManager.getActiveUserInfoAll`

**Purpose:** Lists all currently active/logged-in users.

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

### ONVIF User Variants

Dahua also exposes ONVIF-prefixed user management methods:
- `userManager.getONVIFUserInfoAllV20`
- `userManager.getONVIFUserInfoV20`
- `userManager.addONVIFUserInfoV20`
- `userManager.deleteONVIFUserInfoV20`
- `userManager.modifyONVIFUserInfoV20`
- `userManager.getONVIFGroupInfoAllV20`

**[Params TBD — truncated in source]**

---

## DockUser Commands

### `DockUser.getUserInfoAll`

**Purpose:** Lists all dock user information.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `DockUser.addUser`

**Purpose:** Adds a dock user.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## Security Commands

### `Security.getEncryptInfo`

**Purpose:** Requests the camera's RSA public key for secure payload encryption (used by `system.multiSec`).

| Param | Type | Required | Description |
|---|---|---|---|
| (none) | - | - | No params |

---

## PasswdFind Commands

### `PasswdFind.getDescript`

**Purpose:** Gets password recovery method description (email, QR code, security questions).

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

### `PasswdFind.resetPassword`

**Purpose:** Resets password via recovery method.

| Param | Type | Required | Description |
|---|---|---|---|
| method | string | yes | Recovery method type |
| token | string | yes | Recovery verification token |
| newPassword | string | yes | New hashed password |

> **Note:** Uses `/OutsideCmd` endpoint (unauthenticated).

---

## DigitalCertificate Commands

### `DigitalCertificate.importCert`

**Purpose:** Imports a custom SSL/TLS certificate for HTTPS.

| Param | Type | Required | Description |
|---|---|---|---|
| cert | string | yes | PEM certificate data |
| key | string | yes | PEM private key |

---

### `DigitalCertificate.createCert`

**Purpose:** Generates a self-signed certificate on the device.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

### `DigitalCertificate.getCertDescript`

**Purpose:** Gets certificate description/info.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## GB35114Encrypt Commands

### `GB35114Encrypt.getCurrentVKEKInfo`

**Purpose:** Gets Chinese National Standard (GB35114) video encryption VKEK information.

| Param | Type | Required | Description |
|---|---|---|---|
| **[Params TBD]** | - | - | - |

---

## CertManager Commands

### `CertManager.*`

**Purpose:** Certificate management operations.

**[Params TBD — truncated in source. See `system.listMethod` output for your firmware.]**

---

## 802.1X Commands

### `EAP.802_1x.*`

**Purpose:** 802.1X certificate-based network authentication commands.

**[Params TBD — truncated in source]**
