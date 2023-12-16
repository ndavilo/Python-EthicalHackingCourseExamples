import scapy.all as scapy
import argparse

def scan(ip):
    # Creating an ARP request
    arp_request = scapy.ARP(pdst=ip)
    
    # Creating an Ethernet frame
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Combining the Ethernet frame and ARP request
    arp_request_broadcast = broadcast/arp_request
    
    # Sending the request and receiving the response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    # Processing the response
    sorted_list = []
    for element in answered_list:
        sorted_dic = {"ip": element[1].psrc, "MAC": element[1].hwsrc}
        sorted_list.append(sorted_dic)

    return sorted_list

def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t", "--target", dest="ip", help="Target IP / IP range."
    )

    args = parser.parse_args()

    if not args.ip:
        parser.error("[+] Please specify an IP address. Use --help for more info.")
    
    return args

# Example usage:
options = get_arguments()
print(scan(options.ip))
