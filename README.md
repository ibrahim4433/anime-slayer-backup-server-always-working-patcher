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
* **Java JDK** (for compiling and signing)
* **apktool** & **aapt** (required mainly for Termux)

### How to Patch and Build

#### 📱 On Android (via Termux)
You can patch the APK directly on your phone using Termux!
1. Install Termux from F-Droid (do not use the Play Store version).
2. Open Termux and run these commands to set up:
   ```bash
   pkg update -y
   pkg install -y python git openjdk-17 apktool aapt
   ```
3. Clone this repository and move into it:
   ```bash
   git clone https://github.com/ibrahim4433/anime-slayer-backup-server-always-working-patcher.git
   cd anime-slayer-backup-server-always-working-patcher
   ```
4. Place the **original Anime Slayer v1.5.10 APK** in the cloned folder (you can use your file manager to copy it into the Termux directory).
5. Run the script:
   ```bash
   python patch_apk.py
   ```

#### 🪟 On Windows
1. Install **Python** directly from [python.org](https://www.python.org/downloads/) (do NOT use the Microsoft Store version).
2. Install **Java JDK** from [adoptium.net](https://adoptium.net/).
3. Place the **original Anime Slayer v1.5.10 APK** in this repository folder.
4. Run the script from PowerShell or Command Prompt using the Python launcher:
   ```powershell
   py patch_apk.py
   ```

#### 🐧 On Linux / WSL
1. Install dependencies:
   ```bash
   sudo apt update && sudo apt install -y python3 default-jdk
   ```
2. Place the **original APK** in this folder.
3. Run the script:
   ```bash
   python3 patch_apk.py
   ```

### What the script does under the hood:
1. **Decompiles:** Automatically decompiles the original APK to a temporary directory.
2. **Extracts Certificate:** Extracts the original APK certificate (`CERT.RSA`) from metadata.
3. **Generates Spoofer:** Dynamically creates the `SignatureSpoofer` Smali files using the extracted original certificate bytes.
4. **Applies Patches:** Overwrites the original smali files with the mod files inside `patch-files/`.
5. **Rebuilds APK:** Compiles the patched directories back into a new APK. (On Windows, perfectly bypasses NTFS limitations by automatically injecting pristine resources).
6. **Signs APK:** Generates a local keystore on the fly and signs the new build.
7. **Clean up:** Automatically deletes the temporary directory and outputs the ready-to-use APK: **`Anime_Slayer_v1.5.10_Patched_Working.apk`**.

---

## 💡 Porting to Future Versions

When a new version of the app is released, you only need to:
1. Decompile the new APK.
2. Extract the modifications from `App.smali`, `ServerAdapter.smali`, and `ServerAdapter$ServerHolder.smali` and apply them to the new version's corresponding files.
3. Put those newly patched files into `patch-files/`.
4. Run `python3 patch_apk.py`.
