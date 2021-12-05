class HSRP :
    def __init__(self, packet) :
        self.HsrpPacket = packet.hsrp
        self.packet = packet

    def GetSourceRouter(self) :
        return str(self.packet.ip.src)

    def GetDestRouter(self) :
        return str(self.packet.ip.dst)

    def GetRouterMode(self) :
        routerMode = int(self.HsrpPacket.opcode)
        if routerMode == 0 :
            return str("Hello")
        elif routerMode == 3 :
            return str("Advertise")

    def GetRouterState(self) :
        routerState = int(self.HsrpPacket.state)
        if routerState == 16 :
            return str("Active")
        elif routerState == 8 :
            return str("Standby")
        elif routerState == 3 :
            return str("Passive")
        elif routerState == 8 :
            return str("Standby")

    def GetVirtualIp(self) :
        return str(self.HsrpPacket.virt_ip)

    def GetHelloTime(self) :
        return int(self.HsrpPacket.hellotime)

    def GetHoldTime(self) :
        return int(self.HsrpPacket.holdtime)

    def GetOpCode(self) :
        return int(self.HsrpPacket.opcode)

    def GetPriority(self) :
        return int(self.HsrpPacket.priority)

    def GetAuthData(self) :
        return str(self.HsrpPacket.auth_data)

    def GetVersion(self):
        return int(self.HsrpPacket.version)

    def GetGroup(self) :
        return str(self.HsrpPacket.auth_data)

    def GetReserved(self):
        return int(self.HsrpPacket.version)

    @property
    def ToString(self) :
        if int(self.HsrpPacket.opcode) == 0 :
            result = ("Source Router: " + str(self.GetSourceRouter()) + "\n" +
                      "Destination Router: " + str(self.GetSourceRouter()) + "\n" +
                      "Router Mode: " + str(self.GetRouterMode()) + "\n" +
                      "Router State: " + str(self.GetRouterState()) + "\n" +
                      "Auth_Data: " + str(self.GetAuthData()) + "\n" +
                      "Hello Time: " + str(self.GetHelloTime()) + "\n" +
                      "Hold Time: " + str(self.GetHoldTime()) + "\n" +
                      "OpCode: " + str(self.GetOpCode()) + "\n" +
                      "Virtual IP: " + str(self.GetVirtualIp()) + "\n")
        else :
            result = ("Source Router: " + str(self.GetSourceRouter()) + "\n" +
                      "Destination Router: " + str(self.GetSourceRouter()) + "\n" +
                      "Router Mode: " + str(self.GetRouterMode()) + "\n" +
                      "OpCode: " + str(self.GetOpCode()) + "\n")
        return str(result)
