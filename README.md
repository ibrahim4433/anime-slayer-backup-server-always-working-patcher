# Anime Slayer Patched Source & Automated Build Tool

This repository provides an automated patch utility and the modified Smali files for **Anime Slayer v1.5.10**. 

Unlike full decompiled sources, this repository is lightweight (~80 KB), legal, and contains **only the modified files and a pipeline script** to patch the original APK on the fly.

---

## 📖 Discoveries & Core Architecture

To modify the app without breaking its core features, two major hurdles were analyzed and resolved:

### 1. Dynamic Signature Spoofing (Native Library Bypass)
* **The Problem:** The app's video link resolver relies on a native library (`libnative-lib.so`). This library calls internal Android APIs to retrieve the running APK's signature. If the signature doesn't match the original developer's signature (e.g., when rebuilt and signed with a custom keystore), the native decryption methods (`DriveUtil.a()`) return invalid tokens, causing server requests to fail.
* **The Solution:** We implemented a runtime **Signature Spoofer** in Smali. At application startup (`App.onCreate`), we hook into the Android system's package manager instance using a dynamic proxy (`java.lang.reflect.Proxy`) for `android.content.pm.IPackageManager`. Whenever the native library queries the signature of this application, our spoofer intercepts the query and returns the bytes of the **original certificate** instead of our custom build's signature.

### 2. Backup Server Force Enable
* **The Problem:** The "Backup Server" in the server list is hardcoded to be disabled (unclickable) by default. The app only enables it when it detects that all other external servers are offline ("dead", status `t0.f15791s`).
* **The Solution:** We patched the helper method `isExternalServerAllDead()` inside the server adapter. By modifying this method in `ServerAdapter.smali` to always return `true`, and updating `ServerHolder.bind()` to force-enable the backup server model layout properties, we keep the backup server button **permanently active, green, and clickable** while preserving the functional behavior of the rest of the app.

---

## ⚠️ Important Limitation: Google Sign-In
* **Note:** Because the patched app is resigned with a custom certificate, **"Login with Google" will not work**. Google Play Services verifies the app signature at the OS level (which our client-side spoofer cannot bypass) and compares it with the developer console registration. 
* **Workaround:** Please use the **Email Login** feature instead. It works perfectly with the patched APK.

---

## 🛠️ Mod patches in this Repo (`patch-files/`)

* **`com/anslayer/App.smali`**
  * *Change:* Injects `SignatureSpoofer` initialization hook at `onCreate()`.
* **`com/anslayer/ui/servers/ServerAdapter.smali`**
  * *Change:* Overrides `isExternalServerAllDead()Z` to always return `true`.
* **`com/anslayer/ui/servers/ServerAdapter$ServerHolder.smali`**
  * *Change:* Explicitly forces backup server to have `j = true` (enabled flag) and `h = t0.r` (green working stamp) when binding view.

*(The Signature Spoofer itself is dynamically generated based on the original APK certificate and injected during the build process)*

## 🚀 Build & Patch Automation

We have provided a fully self-contained, cross-platform automation script `patch_apk.py` that handles the entire pipeline on both **Windows** and **Linux/WSL**.

### Prerequisites
* **Python 3.x**
* **Java Development Kit (JDK)** (for compiler execution, signing, and key generation)
* *(Note: `apktool` and `openssl` are NOT required! The script will automatically download `apktool.jar` if missing, and certificate extraction is done in pure Python).*

### How to Patch and Build
1. Place the **original Anime Slayer v1.5.10 APK** in this repository folder.
2. Run the script:
   * **Linux/WSL:** `python3 patch_apk.py`
   * **Windows:** `python patch_apk.py`

### What the script does under the hood:
1. **Decompiles:** Automatically decompiles the original APK to a temporary directory.
2. **Extracts Certificate:** Extracts the original APK certificate (`CERT.RSA`) from metadata and converts it to DER.
3. **Generates Spoofer:** Dynamically creates the `SignatureSpoofer` Smali files wrapping the extracted original certificate.
4. **Applies Patches:** Overwrites the original smali files in the decompiled directory with the mod files inside `patch-files/`.
5. **Rebuilds APK:** Compiles the patched directories back into a new APK.
6. **Signs APK:** Generates a local keystore on the fly (if it doesn't exist) and signs the new build.
7. **Clean up:** Automatically deletes the temporary decompile directory and outputs the ready-to-use APK: **`Anime_Slayer_v1.5.10_Patched_Working.apk`**.

---

## 💡 Porting to Future Versions

When a new version of the app is released, you only need to:
1. Decompile the new APK.
2. Extract the modifications from `App.smali`, `ServerAdapter.smali`, and `ServerAdapter$ServerHolder.smali` and apply them to the new version's corresponding files.
3. Put those newly patched files into `patch-files/`.
4. Run `python3 patch_apk.py`.
