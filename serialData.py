import serial
import serial.tools.list_ports as serialPorts


class portScales:
    accumulatedMass = 0
    portsNames = None

    def __init__(self):
        self.portsNames = self.portDiscovery()

    def portDiscovery(self):
        ports = serialPorts.comports()
        portsName = []
        for i in ports:
            portsName.append(i[0])
        return tuple(portsName)

    def readData(self, protName):
        port = serial.Serial()
        port.port = protName
        port.baudrate = 115200
        port.bytesize = 7
        port.parity = 'N'
        port.stopbits = 1
        port.open()
        while True:
            try:
                s = port.readline()
                print(s)
            except BaseException as exc:
                print(exc)

        port.close()
