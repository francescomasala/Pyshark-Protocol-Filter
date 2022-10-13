import pyshark
from Lib import dhcp


# Sniffing from file
def FileCapture(filePath) :
    print(f'Initiating File Capture on: {filePath}\n')
    cap = pyshark.FileCapture(filePath, display_filter="bootp")
    for packet in cap :
        MyLib = dhcp.DHCPv4(packet)
        print(MyLib.ToString)

# Infinite Sniffing
def LiveCapture(interface) :
    print(f'Initiating Live Capture on: {interface}\n')
    cap = pyshark.LiveCapture(interface=interface)
    for packet in cap.sniff_continuously():
        print(packet.ip.dst)


if __name__ == '__main__' :
    FileCapture('Wireshark_Files/dhcp.pcap')
