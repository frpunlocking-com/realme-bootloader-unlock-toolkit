# Realme Bootloader Unlock Toolkit

Visit the project page for DIY unlocking and tools: [https://frpunlocking.com](https://frpunlocking.com). This tool is needed to get the Unlock key from Realme servers and save it for later use.

## Table of Contents

- [Realme Bootloader Unlock Toolkit](#realme-bootloader-unlock-toolkit)
- [Requirements](#requirements)
  - [Virtual Environment (Recommended)](#virtual-environment-recommended)
- [Usage](#usage)
- [Realme Server Response Codes Explained](#realme-server-response-codes-explained)
  - [Code -1008](#code--1008)
  - [Code -1003](#code--1003)
  - [Code 200 - Success](#code-200--success)
  - [Timestamp-Based Outpot](#timestamp-based-outpot)
- [Security Note](#security-note)
- [Reference](#reference)

## Requirements

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

## 🚀

## Usage

After capturing the ADB log output (`bl.txt`) when apply with [Realme Deeptest GT5 APK](https://frpunlocking.com/diy-unlock/realme-bootloader-unlock/) using:

```bash
adb logcat > bl.txt
```

Run the script using:

```bash
python send.py
```

Make sure to configure your webhook URL and keys appropriately in the script or via environment variables (future version).

## 🖧

## Realme Server Response Codes Explained

When submitting your unlock request or parsing `bl.txt` output, you may encounter server responses like the following:

### Code `-1008`

```json
{"code": -1008, "message": "未提交申请，请先提交解锁申请"}
```

**Translation:**  
*No application submitted. Please submit an unlock request first.*

**Resolution:**  
Make sure you have submitted your unlock application in the **Deeptest GT5 app** and generated logs via ADB.  
👉 [See full guide here](https://frpunlocking.com/how-to-unlock-bootloader-of-a-realme-device/)

---

### Code `-1003`

```json
{"code": -1003, "message": "申请不成功，30天内不能重复申请"}
```

**Translation:**  
*Application unsuccessful. You cannot apply again within 30 days.*

**Resolution:**  
Wait 30 days or use a **different HeyTap account** to retry the unlock process.

---

### Code `200` – Success

```json
{"code": 200, "message": "SUCCESS", "data": {"unlockCode": "your-unlock-key"}}
```

**Meaning:**  
The unlock key has been successfully issued. The `unlockCode` contains the full bootloader unlock token.

**Next step:**  
Use this key with:

```bash
fastboot flashing unlock
```

to complete the unlock process.

---

### 🕒

### Timestamp-Based Outpot

Some server responses may contain a **UNIX timestamp**, indicating when the device is eligible for unlocking.

**Interpretation:**  
This marks the expected time after which the bootloader can be safely unlocked.  
Use tools like [unixtimestamp.com](https://www.unixtimestamp.com/) to convert it to a human-readable format.

## Security Note

Always handle bootloader unlock keys with care. Consider storing them securely and never share them publicly. Unlocking your device may void the warranty and disable certain security features.

## Warranty & Liability Disclaimer

Are you device owner and... your warranty is still valid?

I am not responsible if you brick your device, kill your SD card, install viruses, burn the battery, trigger thermonuclear war, or lose your job because the alarm app failed. Please research any features included in this software **before flashing it! You must be the rightful owner of the device you are modifying and have the legal right to alter its software.**. You are choosing to make these strong modifications on your device, and if you point the finger at me for messing up your device, I will laugh at you.


## Reference

Based on:
- [FRP Unlocking](https://frpunlocking.com)
- [XDA Deeptest GT5 Unlock Guide](https://forum.xda-developers.com/t/guide-bootloader-unlock-for-realme-android-13-14-models-via-deeptest-gt-5.4632127/)
- [ADB logcat usage](https://developer.android.com/studio/command-line/logcat)
- [Fastboot unlocking process](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking)
