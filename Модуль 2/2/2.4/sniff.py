# import scapy.all as scapy
#
# def sniff(interface):
#     scapy.sniff(count= 10, iface = interface, store = False, prn = sniff_func)
#
# def sniff_func(packet):
#     print(packet)
#
# sniff('wlan')
#
# # sniff (count = 10)

import scapy.all as scapy

def sniffing_counter(interface):
    a = scapy.sniff(iface = interface, count = 10)
    a.nsummary()

sniffing_counter("wlan")