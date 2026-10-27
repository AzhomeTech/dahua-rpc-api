# NVR NEXT 固件 (DHI-NVR5xxx-EI) 逆向筆記

實測平台：DAHUA **NVR5232-EI**（NVR NEXT 新版 web 固件），逆向日期：2026-10-27/28。

原 repo 嘅兩步 Challenge-Response MD5 流程 **唔適用於呢版固件**（實測回 `268632085 User or password not valid`）。以下為經真實登入數據驗證嘅正確流程。

## 登入流程（實測 result:true）

### Step 1 — 空密碼攞 challenge

```
POST /RPC2_Login
{"method":"global.login","params":{"userName":"<user>","password":"","clientType":"Web3.0"},"id":1}
```

回應（`268632079 login challenge`）帶：
- `params.random` — nonce
- `params.realm` — `Login to <device-hash>`
- `session` — 下一步要帶

### Step 2 — 兩步 MD5（**大寫**）

```
H1  = MD5("<user>:<realm>:<password>").UPPER()
H2  = MD5("<user>:<random>:<H1>").UPPER()
```

```
POST /RPC2_Login
{"method":"global.login","params":{"userName":"<user>","password":"***","clientType":"Web3.0","authorityType":"Default","passwordType":"Default"},"id":2,"session":"<step1 session>"}
```

成功回：`{"result":true,"session":"<auth session>","params":{"keepAliveInterval":60}}`

⚠️ 注意：
- **必須大寫**（小寫版實測失敗）。原 repo `getAuth()` 嘅小寫公式係舊固件行為。
- challenge session 一次過／短時效，失败會扣 `remainLoginTimes`，用完 lock 30 分鐘。
- 登入後 60 秒內要 call `global.keepAlive` 或者完成晒業務請求。

### 業務 API

帶 `session` POST 去 **`/RPC2`**（唔係 RPC2_Login）。

## 錯誤碼語義（實測）

| Code | 含義 |
|---|---|
| 268632079 | login challenge（正常，step 1） |
| 268632085 | 密碼 hash 唔啱 |
| 268894210 | Method not found |
| 285278249 | **Authority check failure — 對低權限帳號，任何未授權方法（包括完全唔存在嘅方法名）都回呢個碼**。只有 admin 級帳號先可以區分「方法不存在」vs「無權限」。 |

## 低權限帳號實測可用方法（result:true）

- `global.getCurrentTime`
- `magicBox.getDeviceType` → `DHI-NVR5xxx-EI`
- `magicBox.getSerialNo`
- `userManager.getAuthorityList` → `Monitor_01..N`（通道權限組清單）
- `system.listService` → **260 個服務名**（呢版固件完整 namespace 清單）
- `system.listMethod`（只回 system.* 11 個）
- `system.getCaps`、`system.getAPIVersion`

業務數據（ChannelManager/media/configManager/storage/log）需要喺 NVR 用戶管理為帳號分配權限組後先可用。

## 新舊版固件對照（原 repo 方法名失效清單）

新版 web（webpack chunks：`vendors~project.*.chunk.js` 內含 `rpcLib`，`46.*.chunk.js` 含 login）：

- 舊 `configManager.getDeviceType` → 新 **`magicBox.getDeviceType`**
- 舊 `configManager.getBasicInfo` → 未確認（新固件有 `magicBox.getWebInfo` / `ProductWebcaps.get`）
- 通道方法 → `ChannelManager.*` / `media.*` / `mediaapi.getchnlsingle`（待權限解鎖後驗證）
- 舊版 `setNetworkPort` / `addUser` 等 config 方法大概率全部轉咗 `magicBox.*` / `config.*` namespace（chunk 入面見到 `configManager.get(18 refs)/set(19)` 仍然有 export，待驗證實際可用性）

Chunk 內仲見到另一條 **GB35114 網站登入通道**：`POST /ezapi/sys/webLogin/first|second`，用標準 RFC2617 Digest（MD5 六字段 + `Cnonce`/`Nc`/`Algorithm` 欄位），同 RPC2_Login 兩套並行。

## system.methodSignature / methodHelp

呢版固件對 param 格式極嚴：`params:"<name>"`、`params:["<name>"]`、`params:{"method":"<name>"}` 全部回 `268894211 Request invalid param!`。低權限帳號無法探簽名。

## 完整實作參考

見 `python/dahua_nvrnext_login.py`（本 repo fork 加添）。
