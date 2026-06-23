#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil
import glob
import urllib.request
import zipfile

def run_command(cmd, shell=True):
    print(f"Executing: {cmd}")
    result = subprocess.run(cmd, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {cmd}")
        print(f"Stdout:\n{result.stdout}")
        print(f"Stderr:\n{result.stderr}")
        return False, result.stdout, result.stderr
    return True, result.stdout, result.stderr

def format_byte(b):
    sb = b if b < 128 else b - 256
    if sb < 0:
        return f"-0x{abs(sb):x}t"
    else:
        return f"0x{sb:x}t"

def extract_cert_from_pkcs7(data, offset=0):
    while offset < len(data):
        if offset + 2 > len(data):
            break
        tag = data[offset]
        len_byte = data[offset + 1]
        idx = offset + 2
        if len_byte & 0x80:
            num_bytes = len_byte & 0x7f
            if idx + num_bytes > len(data):
                break
            length = 0
            for _ in range(num_bytes):
                length = (length << 8) | data[idx]
                idx += 1
        else:
            length = len_byte
        if tag == 0xa0:
            if idx + 2 <= len(data) and data[idx] == 0x30:
                c_len_byte = data[idx+1]
                v_idx = idx + 2
                if c_len_byte & 0x80:
                    v_idx += (c_len_byte & 0x7f)
                if v_idx < len(data) and data[v_idx] == 0x30:
                    c_tag = data[idx]
                    c_idx = idx + 2
                    if c_len_byte & 0x80:
                        c_num_bytes = c_len_byte & 0x7f
                        c_length = 0
                        for _ in range(c_num_bytes):
                            c_length = (c_length << 8) | data[c_idx]
                            c_idx += 1
                    else:
                        c_length = c_len_byte
                    cert_end = c_idx + c_length
                    if cert_end <= len(data):
                        return data[idx:cert_end]
        if tag in (0x30, 0x31, 0xa0):
            res = extract_cert_from_pkcs7(data[idx:idx+length])
            if res is not None:
                return res
        offset = idx + length
    return None

def extract_cert_from_apk(apk_path):
    try:
        with zipfile.ZipFile(apk_path, 'r') as z:
            for name in z.namelist():
                if name.startswith("META-INF/") and (name.endswith(".RSA") or name.endswith(".DSA")):
                    print(f"[+] Extracting original signature metadata ({name})...")
                    pkcs7_bytes = z.read(name)
                    return extract_cert_from_pkcs7(pkcs7_bytes)
    except Exception as e:
        print(f"[-] Failed to read original signature from APK: {e}")
    return None

def generate_spoofer_files(cert_bytes, output_dir):
    formatted_bytes = "\n        ".join(format_byte(b) for b in cert_bytes)
    cert_len = len(cert_bytes)

    # 1. SignatureSpoofer.smali
    spoofer_template = """.class public Lcom/anslayer/SignatureSpoofer;
.super Ljava/lang/Object;
.source "SignatureSpoofer.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static getCertBytes()[B
    .locals 1

    const/16 v0, __CERT_LEN__

    new-array v0, v0, [B

    fill-array-data v0, :array_0

    return-object v0

    nop

    :array_0
    .array-data 1
        __CERT_BYTES__
    .end array-data
.end method

.method public static hook(Landroid/content/Context;)V
    .locals 7

    # Bypass hidden api checks
    :try_start_api
    const-string v0, "dalvik.system.VMRuntime"

    invoke-static {v0}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v0

    const-string v1, "getRuntime"

    const/4 v2, 0x0

    new-array v3, v2, [Ljava/lang/Class;

    invoke-virtual {v0, v1, v3}, Ljava/lang/Class;->getDeclaredMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v1

    const/4 v3, 0x0

    new-array v4, v2, [Ljava/lang/Object;

    invoke-virtual {v1, v3, v4}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    const-string v3, "setHiddenApiExemptions"

    const/4 v4, 0x1

    new-array v4, v4, [Ljava/lang/Class;

    const-class v5, [Ljava/lang/String;

    aput-object v5, v4, v2

    invoke-virtual {v0, v3, v4}, Ljava/lang/Class;->getDeclaredMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v0

    const/4 v3, 0x1

    new-array v3, v3, [Ljava/lang/Object;

    const-string v4, "L"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v4

    aput-object v4, v3, v2

    invoke-virtual {v0, v1, v3}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;
    :try_end_api
    .catch Ljava/lang/Exception; {:try_start_api .. :try_end_api} :catch_api

    goto :goto_api

    :catch_api
    move-exception v0

    :goto_api

    :try_start_0
    const-string v0, "android.app.ActivityThread"

    invoke-static {v0}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v0

    const-string v1, "currentActivityThread"

    const/4 v2, 0x0

    new-array v3, v2, [Ljava/lang/Class;

    invoke-virtual {v0, v1, v3}, Ljava/lang/Class;->getDeclaredMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v0

    const/4 v1, 0x0

    new-array v3, v2, [Ljava/lang/Object;

    invoke-virtual {v0, v1, v3}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    const-string v1, "android.app.ActivityThread"

    invoke-static {v1}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v1

    const-string v3, "sPackageManager"

    invoke-virtual {v1, v3}, Ljava/lang/Class;->getDeclaredField(Ljava/lang/String;)Ljava/lang/reflect/Field;

    move-result-object v1

    const/4 v3, 0x1

    invoke-virtual {v1, v3}, Ljava/lang/reflect/Field;->setAccessible(Z)V

    invoke-virtual {v1, v0}, Ljava/lang/reflect/Field;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v3

    const-string v4, "android.content.pm.IPackageManager"

    invoke-static {v4}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/Class;->getClassLoader()Ljava/lang/ClassLoader;

    move-result-object v4

    const-string v5, "android.content.pm.IPackageManager"

    invoke-static {v5}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v5

    const/4 v6, 0x1

    new-array v6, v6, [Ljava/lang/Class;

    aput-object v5, v6, v2

    new-instance v5, Lcom/anslayer/SignatureSpoofer$1;

    invoke-direct {v5, p0, v3}, Lcom/anslayer/SignatureSpoofer$1;-><init>(Landroid/content/Context;Ljava/lang/Object;)V

    invoke-static {v4, v6, v5}, Ljava/lang/reflect/Proxy;->newProxyInstance(Ljava/lang/ClassLoader;[Ljava/lang/Class;Ljava/lang/reflect/InvocationHandler;)Ljava/lang/Object;

    move-result-object v4

    invoke-virtual {v1, v0, v4}, Ljava/lang/reflect/Field;->set(Ljava/lang/Object;Ljava/lang/Object;)V

    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v1

    const-string v2, "mPM"

    invoke-virtual {v1, v2}, Ljava/lang/Class;->getDeclaredField(Ljava/lang/String;)Ljava/lang/reflect/Field;

    move-result-object v1

    const/4 v2, 0x1

    invoke-virtual {v1, v2}, Ljava/lang/reflect/Field;->setAccessible(Z)V

    invoke-virtual {v1, v0, v4}, Ljava/lang/reflect/Field;->set(Ljava/lang/Object;Ljava/lang/Object;)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception v0

    invoke-virtual {v0}, Ljava/lang/Exception;->printStackTrace()V

    :goto_0
    return-void
.end method
"""
    spoofer_smali = spoofer_template.replace("__CERT_LEN__", str(cert_len)).replace("__CERT_BYTES__", formatted_bytes)

    # 2. SignatureSpoofer$1.smali
    handler_smali = """.class final Lcom/anslayer/SignatureSpoofer$1;
.super Ljava/lang/Object;
.source "SignatureSpoofer.java"

# interfaces
.implements Ljava/lang/reflect/InvocationHandler;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/anslayer/SignatureSpoofer;->hook(Landroid/content/Context;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x8
    name = null
.end annotation


# instance fields
.field final synthetic val$context:Landroid/content/Context;

.field final synthetic val$sPackageManager:Ljava/lang/Object;


# direct methods
.method constructor <init>(Landroid/content/Context;Ljava/lang/Object;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/anslayer/SignatureSpoofer$1;->val$context:Landroid/content/Context;

    iput-object p2, p0, Lcom/anslayer/SignatureSpoofer$1;->val$sPackageManager:Ljava/lang/Object;

    return-void
.end method


# virtual methods
.method public invoke(Ljava/lang/Object;Ljava/lang/reflect/Method;[Ljava/lang/Object;)Ljava/lang/Object;
    .locals 7

    invoke-virtual {p2}, Ljava/lang/reflect/Method;->getName()Ljava/lang/String;

    move-result-object p1

    const-string v0, "getPackageInfo"

    invoke-virtual {v0, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_4

    const/4 p1, 0x0

    aget-object p1, p3, p1

    check-cast p1, Ljava/lang/String;

    iget-object v0, p0, Lcom/anslayer/SignatureSpoofer$1;->val$context:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v0, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_4

    const/4 p1, 0x0

    array-length v0, p3

    const/4 v1, 0x0

    :goto_0
    if-ge v1, v0, :cond_2

    aget-object v2, p3, v1

    instance-of v3, v2, Ljava/lang/Integer;

    if-eqz v3, :cond_0

    check-cast v2, Ljava/lang/Integer;

    invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I

    move-result p1

    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    goto :goto_1

    :cond_0
    instance-of v3, v2, Ljava/lang/Long;

    if-eqz v3, :cond_1

    check-cast v2, Ljava/lang/Long;

    invoke-virtual {v2}, Ljava/lang/Long;->intValue()I

    move-result p1

    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    goto :goto_1

    :cond_1
    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    :cond_2
    :goto_1
    if-eqz p1, :cond_4

    invoke-virtual {p1}, Ljava/lang/Integer;->intValue()I

    move-result p1

    and-int/lit8 p1, p1, 0x40

    if-eqz p1, :cond_4

    iget-object p1, p0, Lcom/anslayer/SignatureSpoofer$1;->val$sPackageManager:Ljava/lang/Object;

    invoke-virtual {p2, p1, p3}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Landroid/content/pm/PackageInfo;

    if-eqz p1, :cond_3

    new-instance v0, Landroid/content/pm/Signature;

    invoke-static {}, Lcom/anslayer/SignatureSpoofer;->getCertBytes()[B

    move-result-object v1

    invoke-direct {v0, v1}, Landroid/content/pm/Signature;-><init>([B)V

    const/4 v1, 0x1

    new-array v1, v1, [Landroid/content/pm/Signature;

    const/4 v2, 0x0

    aput-object v0, v1, v2

    iput-object v1, p1, Landroid/content/pm/PackageInfo;->signatures:[Landroid/content/pm/Signature;

    return-object p1

    :cond_3
    const/4 p1, 0x0

    return-object p1

    :cond_4
    iget-object p1, p0, Lcom/anslayer/SignatureSpoofer$1;->val$sPackageManager:Ljava/lang/Object;

    invoke-virtual {p2, p1, p3}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p1

    return-object p1
.end method
"""

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "SignatureSpoofer.smali"), "w") as f:
        f.write(spoofer_smali)
    with open(os.path.join(output_dir, "SignatureSpoofer$1.smali"), "w") as f:
        f.write(handler_smali)
    print(f"[+] Wrote dynamic SignatureSpoofer smali files to {output_dir}")

def copy_folder_recursive(src, dst):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            os.makedirs(d, exist_ok=True)
            copy_folder_recursive(s, d)
        else:
            shutil.copy2(s, d)

def download_apktool():
    url = "https://github.com/iBotPeaches/Apktool/releases/download/v2.9.3/apktool_2.9.3.jar"
    local_path = "apktool.jar"
    print(f"[+] Downloading apktool.jar from {url}...")
    try:
        urllib.request.urlretrieve(url, local_path)
        print("[+] Download complete.")
        return True
    except Exception as e:
        print(f"[-] Failed to download apktool.jar: {e}")
        print("    Please download it manually and place it in this folder as 'apktool.jar'")
        return False

def get_apktool_command(java_cmd):
    # Check if local apktool.jar exists
    if os.path.exists("apktool.jar"):
        if java_cmd:
            return f'"{java_cmd}" -jar "apktool.jar"'
    
    # Check if apktool is in PATH
    apktool_cmd = shutil.which("apktool")
    if apktool_cmd:
        return f'"{apktool_cmd}"'
    
    # Download apktool.jar if missing
    if download_apktool():
        if java_cmd:
            return f'"{java_cmd}" -jar "apktool.jar"'
            
def find_java_windows():
    if sys.platform != 'win32':
        return None
    # Check common install directories for Java
    program_files = os.environ.get("ProgramFiles", "C:\\Program Files")
    program_files_x86 = os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)")
    
    scan_dirs = [
        os.path.join(program_files, "Eclipse Adoptium"),
        os.path.join(program_files, "Eclipse Foundation"),
        os.path.join(program_files, "Java"),
        os.path.join(program_files, "Microsoft"),
        os.path.join(program_files_x86, "Java"),
    ]
    
    for base in scan_dirs:
        if os.path.exists(base):
            for root, dirs, files in os.walk(base):
                if "java.exe" in files:
                    # Verify it has keytool and jarsigner adjacent
                    if "keytool.exe" in files and "jarsigner.exe" in files:
                        return os.path.join(root, "java.exe")
    return None

def main():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(repo_dir)

    print("=== Anime Slayer APK Automated Patch Utility ===")

    # 1. Check requirements (Java)
    java_cmd = shutil.which("java")
    if not java_cmd and sys.platform == 'win32':
        # Try to locate Java automatically in typical Windows installation folders
        java_cmd = find_java_windows()

    if not java_cmd:
        print("[-] Java not found in system PATH or standard directories!")
        if sys.platform != 'win32':
            print("    Please run: sudo apt update && sudo apt install -y default-jdk")
        else:
            print("    Please install Java JDK/JRE from: https://adoptium.net/")
            print("    (If you just installed it, please restart VS Code/your terminal to refresh your environment variables)")
        sys.exit(1)

    keytool_cmd = shutil.which("keytool")
    if not keytool_cmd:
        # Check adjacent directory
        java_dir = os.path.dirname(java_cmd)
        potential_keytool = os.path.join(java_dir, "keytool" + (".exe" if sys.platform == "win32" else ""))
        if os.path.exists(potential_keytool):
            keytool_cmd = potential_keytool
        else:
            print("[-] keytool not found! Make sure Java JDK (not JRE) is installed.")
            sys.exit(1)

    jarsigner_cmd = shutil.which("jarsigner")
    if not jarsigner_cmd:
        # Check adjacent directory
        java_dir = os.path.dirname(java_cmd)
        potential_jarsigner = os.path.join(java_dir, "jarsigner" + (".exe" if sys.platform == "win32" else ""))
        if os.path.exists(potential_jarsigner):
            jarsigner_cmd = potential_jarsigner
        else:
            print("[-] jarsigner not found! Make sure Java JDK (not JRE) is installed.")
            sys.exit(1)

    # Resolve apktool
    apktool_cmd = get_apktool_command(java_cmd)
    if not apktool_cmd:
        print("[-] apktool wrapper/jar not found and download failed!")
        sys.exit(1)

    # 2. Locate original APK file
    apk_files = glob.glob(os.path.join(repo_dir, "*v1.5.10*.apk"))
    if not apk_files:
        apk_files = glob.glob(os.path.join(repo_dir, "*.apk"))
        # Exclude output patches
        apk_files = [f for f in apk_files if "_Patched_" not in f and "-patched" not in f]

    if not apk_files:
        print("[-] Original Anime Slayer APK not found in current directory!")
        print("    Please place the original Anime Slayer v1.5.10 APK file in this folder.")
        sys.exit(1)

    target_apk = apk_files[0]
    print(f"[+] Found Target APK: {os.path.basename(target_apk)}")

    # Check readability of input APK (permissions check on WSL/Linux)
    if not os.access(target_apk, os.R_OK):
        print(f"[-] Error: Input file '{os.path.basename(target_apk)}' is not readable!")
        if sys.platform != 'win32':
            # WSL / Linux path permission issue
            print("    Your WSL environment does not have read permissions for this file.")
            print("    Please run the following command to fix it:")
            print(f'    sudo chmod 644 "{target_apk}"')
        else:
            print("    Please check the read permissions of this APK file.")
        sys.exit(1)

    # 3. Extract original certificate from APK ZIP directory directly
    cert_bytes = extract_cert_from_apk(target_apk)
    if not cert_bytes:
        print("[-] Failed to extract original certificate from the APK!")
        sys.exit(1)
    print(f"[+] Original certificate extracted successfully ({len(cert_bytes)} bytes).")

    temp_dir = os.path.join(repo_dir, "temp-decompiled")
    if os.path.exists(temp_dir):
        print("[+] Cleaning up previous temporary folders...")
        shutil.rmtree(temp_dir)

    # 4. Decompile using apktool (ignoring resources)
    print("[+] Decompiling APK (ignoring resources for speed and compatibility)...")
    success, _, _ = run_command(f'{apktool_cmd} d -r "{target_apk}" -o "{temp_dir}"')
    if not success:
        print("[-] Decompilation failed.")
        sys.exit(1)

    # 5. Generate dynamic SignatureSpoofer smali files
    spoofer_dir = os.path.join(temp_dir, "smali", "com", "anslayer")
    generate_spoofer_files(cert_bytes, spoofer_dir)

    # 6. Overwrite/apply patches from patch-files folder
    patches_src = os.path.join(repo_dir, "patch-files")
    if not os.path.exists(patches_src):
        print("[-] patch-files folder not found! Cannot apply mod patches.")
        shutil.rmtree(temp_dir)
        sys.exit(1)

    print("[+] Applying smali patch files to decompiled source...")
    patches_dst = os.path.join(temp_dir, "smali")
    copy_folder_recursive(patches_src, patches_dst)

    # 7. Rebuild APK
    patched_apk = os.path.join(repo_dir, "anime-slayer-patched.apk")
    print("[+] Rebuilding patched APK (assembling smali bytecode)...")
    success, _, _ = run_command(f'{apktool_cmd} b "{temp_dir}" -o "{patched_apk}"')
    if not success:
        print("[-] Compilation failed.")
        shutil.rmtree(temp_dir)
        sys.exit(1)

    # 8. Keystore Handling and Signing
    keystore_path = os.path.join(repo_dir, "local-release-key.jks")
    keystore_alias = "alias_name"
    keystore_pass = "android"

    if not os.path.exists(keystore_path):
        print("[+] Generating temporary release signing key...")
        genkey_cmd = (
            f'"{keytool_cmd}" -genkey -v -keystore "{keystore_path}" -keyalg RSA -keysize 2048 -validity 10000 '
            f'-alias "{keystore_alias}" -storepass "{keystore_pass}" -keypass "{keystore_pass}" '
            f'-dname "CN=Android Debug,O=Android,C=US"'
        )
        success, _, _ = run_command(genkey_cmd)
        if not success:
            print("[-] Keystore generation failed!")
            shutil.rmtree(temp_dir)
            sys.exit(1)

    print("[+] Signing the patched APK...")
    sign_cmd = (
        f'"{jarsigner_cmd}" -verbose -sigalg SHA256withRSA -digestalg SHA-256 '
        f'-keystore "{keystore_path}" -storepass "{keystore_pass}" -keypass "{keystore_pass}" '
        f'"{patched_apk}" "{keystore_alias}"'
    )
    success, _, _ = run_command(sign_cmd)
    if not success:
        print("[-] Signing failed!")
        shutil.rmtree(temp_dir)
        sys.exit(1)

    # 9. Clean up decompiled workspace
    print("[+] Cleaning up decompiled workspace directory...")
    shutil.rmtree(temp_dir)

    final_name = "Anime_Slayer_v1.5.10_Patched_Working.apk"
    final_path = os.path.join(repo_dir, final_name)
    if os.path.exists(patched_apk):
        if os.path.exists(final_path):
            os.remove(final_path)
        shutil.move(patched_apk, final_path)

    print(f"\n[+] SUCCESS! Final patched and signed APK generated at: {final_path}")
    print("    You can now copy and install this file on your device.")

if __name__ == "__main__":
    main()
