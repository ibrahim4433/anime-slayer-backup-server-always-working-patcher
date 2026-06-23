#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil
import glob

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

def generate_spoofer_files(cert_path, output_dir):
    with open(cert_path, "rb") as f:
        cert_bytes = f.read()

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

def main():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(repo_dir)

    print("=== Anime Slayer APK Automated Patch Utility ===")

    # 1. Locate original APK file
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

    temp_dir = os.path.join(repo_dir, "temp-decompiled")
    if os.path.exists(temp_dir):
        print("[+] Cleaning up previous temporary folders...")
        shutil.rmtree(temp_dir)

    # 2. Decompile using apktool
    print("[+] Decompiling APK (this may take a minute)...")
    success, _, _ = run_command(f'apktool d "{target_apk}" -o "{temp_dir}"')
    if not success:
        print("[-] Decompilation failed. Ensure apktool is installed and in your PATH.")
        sys.exit(1)

    # 3. Extract original certificate from decompiled folder
    cert_rsa = os.path.join(temp_dir, "original", "META-INF", "CERT.RSA")
    if not os.path.exists(cert_rsa):
        # Look for other names
        metainf_dir = os.path.join(temp_dir, "original", "META-INF")
        rsa_files = glob.glob(os.path.join(metainf_dir, "*.RSA")) + glob.glob(os.path.join(metainf_dir, "*.DSA"))
        if rsa_files:
            cert_rsa = rsa_files[0]
        else:
            print("[-] Original CERT.RSA not found in decompiled APK metadata!")
            shutil.rmtree(temp_dir)
            sys.exit(1)

    cert_pem = "/tmp/cert.pem"
    cert_der = "/tmp/cert.der"

    print("[+] Extracting original certificate metadata...")
    success, _, _ = run_command(f'openssl pkcs7 -inform DER -in "{cert_rsa}" -print_certs -out "{cert_pem}"')
    if not success:
        shutil.rmtree(temp_dir)
        sys.exit(1)

    success, _, _ = run_command(f'openssl x509 -inform PEM -in "{cert_pem}" -outform DER -out "{cert_der}"')
    if not success:
        shutil.rmtree(temp_dir)
        sys.exit(1)

    # 4. Generate dynamic SignatureSpoofer smali files
    spoofer_dir = os.path.join(temp_dir, "smali", "com", "anslayer")
    generate_spoofer_files(cert_der, spoofer_dir)

    # Clean up temp cert files
    for f in [cert_pem, cert_der]:
        if os.path.exists(f):
            os.remove(f)

    # 5. Overwrite/apply patches from patch-files folder
    patches_src = os.path.join(repo_dir, "patch-files")
    if not os.path.exists(patches_src):
        print("[-] patch-files folder not found! Cannot apply mod patches.")
        shutil.rmtree(temp_dir)
        sys.exit(1)

    print("[+] Applying smali patch files to decompiled source...")
    patches_dst = os.path.join(temp_dir, "smali")
    copy_folder_recursive(patches_src, patches_dst)

    # 6. Rebuild APK
    patched_apk = os.path.join(repo_dir, "anime-slayer-patched.apk")
    print("[+] Rebuilding patched APK (compiling resources)...")
    success, _, _ = run_command(f'apktool b "{temp_dir}" -o "{patched_apk}" --use-aapt2')
    if not success:
        print("[-] Compilation failed with aapt2. Trying normal aapt...")
        success, _, _ = run_command(f'apktool b "{temp_dir}" -o "{patched_apk}"')
        if not success:
            print("[-] Compilation failed completely.")
            shutil.rmtree(temp_dir)
            sys.exit(1)

    # 7. Keystore Handling and Signing
    keystore_path = "/tmp/my-release-key.jks"
    keystore_alias = "alias_name"
    keystore_pass = "android"

    if not os.path.exists(keystore_path):
        print("[+] Generating temporary release signing key...")
        genkey_cmd = (
            f'keytool -genkey -v -keystore "{keystore_path}" -keyalg RSA -keysize 2048 -validity 10000 '
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
        f'jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 '
        f'-keystore "{keystore_path}" -storepass "{keystore_pass}" -keypass "{keystore_pass}" '
        f'"{patched_apk}" "{keystore_alias}"'
    )
    success, _, _ = run_command(sign_cmd)
    if not success:
        print("[-] Signing failed!")
        shutil.rmtree(temp_dir)
        sys.exit(1)

    # 8. Clean up decompiled workspace
    print("[+] Cleaning up decompiled workspace directory...")
    shutil.rmtree(temp_dir)

    final_name = "Anime_Slayer_v1.5.10_Patched_Working.apk"
    final_path = os.path.join(repo_dir, final_name)
    if os.path.exists(patched_apk):
        shutil.move(patched_apk, final_path)

    print(f"\n[+] SUCCESS! Final patched and signed APK generated at: {final_path}")
    print("    You can now copy and install this file on your device.")

if __name__ == "__main__":
    main()
