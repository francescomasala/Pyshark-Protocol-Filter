import json


class DHCPv4 :
    def __init__(self, packet):
        self.DhcpPacket = packet.dhcp
        self.packet = packet

    def GetHighestLayerName(self):
        return self.packet.highest_layer

    def GetSource(self):
        return str(self.packet.ip.src)

    def GetDest(self):
        return str(self.packet.ip.dst)

    def GetDhcpOption(self):
        dhcpOption = int(self.packet.dhcp.option_dhcp)
        if (dhcpOption == 1):
            return "discover"
        elif (dhcpOption == 2):
            return "offer"
        elif (dhcpOption == 3):
            return "request"
        elif (dhcpOption == 5):
            return "acknowledge"
        elif (dhcpOption == 7):
            return "acknowledge"

    def GetDhcpServer(self):
        return str(self.DhcpPacket.option_dhcp_server_id)

    def GetRequestedIP(self):
        return str(self.DhcpPacket.option_requested_ip_address)

    @property
    def ToJson(self) :
        result = {
                "HighestLayer": str(self.GetHighestLayerName()),
                "SourceRouter": str(self.GetSource()),
                "DestinationRouter": str(self.GetDest())
            }
        return json.dumps(result)

    @property
    def ToString(self) :
        result = ("Highest Layer: " + str(self.GetHighestLayerName()) + "\n" +
                  "Source Address: " + str(self.GetSource()) + "\n" +
                  "Destination Address: " + str(self.GetDest()) + "\n" +
                  "DHCP Option: " + str(self.GetDhcpOption()) + "\n"
                  )
        return str(result)