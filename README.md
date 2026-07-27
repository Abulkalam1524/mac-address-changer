# 🔧 MAC Address Changer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey)

A simple Python tool that changes the MAC address of a network interface on Linux systems, built for learning ethical hacking and networking fundamentals.

---

## 📋 Table of Contents
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Demo](#-demo)
- [Disclaimer](#-disclaimer)

---

## ✨ Features
- Displays the current MAC address of a given network interface
- Changes it to a user-specified MAC address
- Verifies whether the change was successful
- Includes root privilege check before making changes

## ⚙️ Requirements
- Linux (uses `ifconfig`, may require the `net-tools` package)
- Python 3
- Root/sudo privileges

## 📦 Installation

```bash
git clone https://github.com/Abulkalam1524/mac-address-changer.git
cd mac-address-changer
```

## 🚀 Usage

```bash
sudo python3 mac_changer.py -i <interface> -m <new_mac_address>
```

**Example:**
```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

**Sample Output:**## 🧠 How It Works
1. Reads the current MAC address of the specified interface using `ifconfig`.
2. Brings the interface down, changes the MAC address, and brings it back up.
3. Re-reads the MAC address to confirm whether the change was successful.

## 📸 Demo
![MAC Changer Demo](demo.png)

## ⚠️ Disclaimer
This project is for **educational purposes only**, built while learning ethical hacking and Python scripting. Only use this tool on devices and networks you own or have explicit permission to test.

---

### 🔗 Related Projects
- [Network Scanner](https://github.com/Abulkalam1524/network-scanner)
