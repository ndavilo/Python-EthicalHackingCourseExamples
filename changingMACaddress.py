import subprocess
import optparse

def get_interfaces():
    interfaces = subprocess.call("ifconfig")
    return interfaces

def change_mac(interface, new_mac):
    print(f"Changing MAC address of {interface} to {new_mac}")

    # Disable the interface
    subprocess.call(["sudo", "ifconfig", interface, "down"])

    # Change the MAC address
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])

    # Enable the interface
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option(
        "-i", "--interface", dest="interface", help="Interface to change its MAC address"
    )
    parser.add_option(
        "-m", "--mac", dest="new_mac", help="New MAC address"
    )

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[+] Please specify an interface. Use --help for more info.")
    elif not options.new_mac:
        parser.error("[+] Please specify a new MAC address. Use --help for more info.")

    return options

get_interfaces()
options = get_arguments()
change_mac(options.interface, options.new_mac)
