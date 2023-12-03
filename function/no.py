import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP()
    arp_request.pdst = ip
    broadcast = scapy.Ether()
    broadcast.dst = "ff:ff:ff:ff:ff:ff"
    arp_request_broadcast = broadcast/arp_request
    list_jawaban = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("IP\t\t\tMac Address\n===========================================")
    for element in list_jawaban:
        print(element[1].psrc+"\t\t"+element[1].hwsrc)


scan("192.168.1.8/24")