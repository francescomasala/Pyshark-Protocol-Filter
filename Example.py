import pyshark
from Lib import Cisco


# Sniffing from file
def FileCapture(filePath) :
    print(f'Initiating File Capture on: {filePath}\n')
    cap = pyshark.FileCapture(filePath, display_filter="hsrp")
    for packet in cap :
        MyLib = Cisco.HSRP(packet)
        print(MyLib.ToString)

# Infinite Sniffing
def LiveCapture(interface) :
    print(f'Initiating Live Capture on: {interface}\n')
    cap = pyshark.LiveCapture(interface=interface)
    for packet in cap.sniff_continuously() :
        print(packet.ip.dst)


if __name__ == '__main__' :
    FileCapture('hsrp_example.pcap')
