#!/usr/bin/env python

import re            # used to search for MAC address patterns using regular expressions
import subprocess     # used to run system commands like ifconfig
import optparse       # used to parse command-line arguments (-i, -m)
import os             # used to check if the script is running as root


def get_arguments():
    """
    Parses command-line arguments.
    User must provide:
      -i / --interface : the network interface (e.g. eth0, wlan0)
      -m / --mac       : the new MAC address to assign
    """
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                       help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac",
                       help="New MAC address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[+] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")

    return options


def check_root():
    """
    Changing a MAC address requires root privileges.
    This function checks if the script is being run with sudo/root.
    If not, it warns the user and stops the script instead of failing silently.
    """
    if os.geteuid() != 0:
        print("[-] This script must be run as root. Try: sudo python3 mac_changer.py -i <interface> -m <new_mac>")
        exit(1)


def change_mac(interface, new_mac):
    """
    Changes the MAC address of the given interface:
    1. Brings the interface down (required before changing MAC)
    2. Sets the new MAC address
    3. Brings the interface back up
    """
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    """
    Runs 'ifconfig <interface>' and extracts the current MAC address
    using a regular expression that matches the standard MAC format
    (six groups of two hex characters separated by colons).
    """
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


# ---- Main program execution ----

# Step 1: Make sure the script is running with root privileges
check_root()

# Step 2: Parse command-line arguments (interface + new MAC)
options = get_arguments()

# Step 3: Read and display the current MAC address before making changes
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

# Step 4: Change the MAC address to the one specified by the user
change_mac(options.interface, options.new_mac)

# Step 5: Read the MAC address again after the change, to confirm it worked
current_mac = get_current_mac(options.interface)

# Step 6: Compare before/after to verify success
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")