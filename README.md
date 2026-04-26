# APOP-Cracker

A Python-based GUI utility designed to perform dictionary attacks against **APOP (Authenticated Post Office Protocol)** authentication captures. This tool automates the manual process of reverse-engineering MD5-hashed challenge-response sequences often found in legacy mail server environments or CTF challenges (e.g., Root-Me).

## How It Works

APOP authentication is designed to avoid sending plaintext passwords. However, it relies on the MD5 hashing algorithm, which is susceptible to brute-force attacks if a weak password is used.

The authentication follows this logic:

1. The server sends a Timestamp (Challenge) in the greeting banner: `<123.abc@host>`
2. The client responds with a **Digest**: `MD5(Timestamp + Password)`
3. This script iterates through a wordlist, reapplying that formula to every entry until a matching hash is found.

## Features

- **GUI Interface:** Built with `tkinter` for easy input of banners and hashes.
- **Flexible Wordlist Selection:** Integrated file browser to select local wordlists (e.g., `rockyou.txt`).
- **Gzip Support:** Automatically detects and reads `.gz` compressed wordlists without manual decompression.
- **Memory Efficient:** Streams wordlists line-by-line to prevent system hangs when using large files (100MB+).
- **Cross-Platform:** Works on Debian (primary lab environment), Kali, and Windows.

## Prerequisites

- Python 3.x
- tkinter (Usually included with Python, or `sudo apt install python3-tk` on Linux)
- A wordlist (e.g., `RockYou`)

## Usage Instructions

1. **Extract Data:** Open your `.pcap` or `.pcapng` file in Wireshark.

2. **Locate APOP session:**

- Find the server's +OK banner (e.g., `<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>`).

- Find the client's APOP command hash (e.g., `4ddd4137b84ff2db7291b568289717f0`).

3. **Run the script:**

``` Bash
python3 apop_cracker.py
```

4. **Input:**

- Paste the full banner (including brackets < >)
- Paste the target hash
- Click Browse to select your wordlist

5. **Execute:** Click **RUN ATTACK**. The status will update once a match is found

---

# ⚠️ Security Disclaimer

This tool is intended for educational purposes and authorized penetration testing/CTF challenges only. Using this tool against servers you do not have explicit permission to test is illegal and unethical
