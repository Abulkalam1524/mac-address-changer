# MAC Address Changer

A simple Python tool that changes the MAC address of a network interface on Linux systems, built for learning ethical hacking and networking fundamentals.

## Features
- Displays the current MAC address of a given network interface
- Changes it to a user-specified MAC address
- Verifies whether the change was successful

## Requirements
- Linux (uses `ifconfig`, may require `net-tools` package)
- Python 3
- Root/sudo privileges

## Installation
```bash
git clone https://github.com/Abulkalam1524/mac-address-changer.git
cd mac-address-changer
```

## Usage
```bash
sudo python3 mac_changer.py -i <interface> -m <new_mac_address>
```

Example:
```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

## How it works
1. Reads the current MAC address of the specified interface using `ifconfig`.
2. Brings the interface down, changes the MAC address, and brings it back up.
3. Re-reads the MAC address to confirm the change was successful.

## Disclaimer
This project is for educational purposes only, built while learning ethical hacking and Python scripting.
