# Core Endpoints & Payload Anatomy

## Endpoints

### `/RPC2_Login`
- **Purpose:** Authentication exclusively (`global.login`)
- **HTTP Method:** POST
- **Content-Type:** application/json
- **Source:** `rpcBase.js`

### `/RPC2`
- **Purpose:** All standard RPC commands
- **HTTP Method:** POST
- **Content-Type:** application/json
- **Source:** `rpcBase.js`

### `/OutsideCmd`
- **Purpose:** Unauthenticated commands (password reset, system initialization)
- **HTTP Method:** POST
- **Content-Type:** application/json

---

## Payload Builder (`rpcBase.js` function `g`)

```javascript
function g(b, c, d) {
    return a.extend({
        method: b,          // The command, e.g., "ptz.start"
        params: c || null,  // The arguments
        id: m++,            // Auto-incrementing counter
        session: e()        // Current session token
    }, d)
}
```

## HTTP Sender (`rpcBase.js` function `sendRPC`)

```javascript
l.sendRPC = function(b, c, d) {
    return a.ajax({
        type: "POST",
        url: b || "/RPC2",
        data: JSON.stringify(c),
        dataType: "json",
        jsonp: !1,
        async: d
    })
}
```

## Response Handler (`rpcBase.js` function `h`)

```javascript
function h(b, c, d) {
    return a.Deferred(function(f) {
        l.sendRPC(c, b, d).done(function(b) {
            b.result ? f.resolve(b) : b.error && b.error.code && 287637504 == b.error.code ?
                (window.fireSessionInvalid = !0,
                 a.publish("SessionInvalid", e()),
                 f.reject(b)) : f.reject(b)
        }).fail(f.reject)
    }).promise()
}
```

- On `result: true` → resolve promise
- On error code `287637504` → session invalid, publish SessionInvalid event
- Other errors → reject promise

## Request Deduplication (`rpc.js` function `d`)

The wrapper in `rpc.js` caches in-flight requests by session + serialized params, avoiding duplicate calls:

```javascript
function d(b) {
    var c = {};
    this.instance = function(d, f) {
        var g = e.getSession(), h = JSON.stringify(a.extend(d, f));
        return c[g] && c[g][h] && "rejected" != c[g][h].state() ? c[g][h] :
               c[g] ? c[g][h] = e.send(b, d, f) : (c = {}, c[g] = {}, c[g][h] = e.send(b, d, f))
    }
}
```

## Encryption Detection (`rpcBase.js` function `i`)

```javascript
function i() {
    var a = "AES-128", b = webApp.EncryptInfo.cipher;
    return ~b.indexOf("ROAE") ? a = "ROAE-256" : ~b.indexOf("RPAC") && (a = "RPAC-256"), a
}
```

Supported ciphers: AES-128, ROAE-256, RPAC-256

## Standard Response Format

```json
{
  "id": 12,
  "params": { ... },
  "result": true,
  "session": "abcdef1234567890"
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Echoes request id |
| `params` | object | Response data |
| `result` | boolean | `true` on success, `false` or absent on error |
| `session` | string | Session token (may be updated) |

## Error Response Format

```json
{
  "id": 12,
  "error": {
    "code": 268632079,
    "message": "Description of the error"
  },
  "result": false,
  "session": "abcdef1234567890"
}
```

| Error Code | Meaning |
|---|---|
| 268632079 | Login challenge required (first login step) |
| 287637504 | Session invalid / expired |
| 401 (HTTP) | Unauthorized / challenge needed |
