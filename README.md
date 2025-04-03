# 🔓 Realme Bootloader Unlock Toolkit to save unlock key

Visit the project page for DIY unlocking and tools: [https://frpunlocking.com](https://frpunlocking.com).

## 📚 Table of Contents

- [🔓 Realme Bootloader Unlock Toolkit to save unlock key](#️-realme-bootloader-unlock-toolkit-to-save-unlock-key)
- [🛠 Requirements](#️-requirements)
  - [Virtual Environment (Recommended)](#virtual-environment-recommended)
- [🚀 Usage](#️-usage)
- [🖧 Explanation of Replies from Realme Severs](#️-explanation-of-replies-from-realme-severs)
  - [Code -1008](#code--1008)
  - [Code -1003](#code--1003)
  - [Code 200](#code-200)
  - [Reply with timestamp](#reply-with-timestamp)
- [🔐 Security Note](#️-security-note)
- [🧠 Reference](#️-reference)

## 🛠 Requirements

Before running the script, make sure you have Python 3.8+ installed. You can install the required dependencies using:

```bash
pip install -r requirements.txt
```

Required Python packages:
- `cryptography` – for decrypting the unlock token
- `requests` – used to send the unlock key via webhook
- `cffi`
- `pycparser`

Using a virtual environment (recommended alternative)
If you plan to install multiple packages or manage dependencies cleanly, you might find it easier to use a virtual environment in your folder:

### Virtual Environment (Recommended)

Create a virtual environment inside your local folder ie. `C:\send`:

```bash
cd C:\send
python -m venv venv
```
Activate the environment:

```bash
C:\send
```

Install cryptography (now it goes into C:\send):

```bash
pip install cffi>=1.17.0 cryptography>=44.0.0 pycparser>=2.22 requests>=2.25.0
```

Run your script:

```bash
python send.py
```

This way, your dependencies remain isolated to that specific virtual environment, and you don’t need to manually insert paths.

## 🚀 Usage

After capturing the ADB log output (`bl.txt`) when apply with [Realme Deeptest GT5 APK](https://frpunlocking.com/diy-unlock/realme-bootloader-unlock/) using:

```bash
adb logcat > bl.txt
```

Run the script using:

```bash
python send.py
```

Make sure to configure your webhook URL and keys appropriately in the script or via environment variables (future version).

## 🖧 Explanation of Replies from Realme Severs

It looks like the server responded with the following JSON message:

### Code -1008

```json
{"code": -1008, "message": "未提交申请，请先提交解锁申请"}
```

Translated from Chinese, the message says:

“No application submitted. Please submit an unlock request first.”

Resolution: [submit in DeepTest GT5 with ADB like on this post](https://frpunlocking.com/how-to-unlock-bootloader-of-a-realme-device/).

### Code -1003

The error message you've encountered:

```json
复制
{"code":-1003,"message":"申请不成功，30天内不能重复申请"}```

translates to: "Application unsuccessful; cannot reapply within 30 days."

Resolution: change HeyTap account or make new one.

### Code 200

```json
Decoded response: {"code":200,"message":"SUCCESS","data":{"unlockCode":"lot-of-chars"}}
```

On unlockCode there was receivied an unlock bootloader code.

### Reply with timestamp

On that Unix timestamp Bootloader should be able to get unlock code.

## 🔐 Security Note

Always handle bootloader unlock keys with care. Consider storing them securely and never share them publicly. Unlocking your device may void the warranty and disable certain security features.

## 🧠 Reference

Based on:
- [FRP Unlocking](https://frpunlocking.com)
- [XDA Deeptest GT5 Unlock Guide](https://forum.xda-developers.com/t/guide-bootloader-unlock-for-realme-android-13-14-models-via-deeptest-gt-5.4632127/)
- [ADB logcat usage](https://developer.android.com/studio/command-line/logcat)
- [Fastboot unlocking process](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking)
