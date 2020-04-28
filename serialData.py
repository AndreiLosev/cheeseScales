import serial
import serial.tools.list_ports as serialPorts


class portScales:
    accumulatedMass = 0
    portsNames = None
    readContin = False
    readUpdate = False

    def __init__(self):
        self.portsNames = self.portDiscovery()

    def stopRead(self):
        self.readContin = False

    def startRead(self):
        self.readContin = True

    def summ(self, newWeight):
        return float(newWeight.decode('ascii'))

    def portDiscovery(self):
        ports = serialPorts.comports()
        portsName = []
        for i in ports:
            portsName.append(i[0])
        return tuple(portsName)

    def readData(self, protName):
        port = serial.Serial()
        port.timeout = 0
        port.port = protName
        port.baudrate = 115200
        port.bytesize = 7
        port.parity = 'N'
        port.stopbits = 1
        port.open()
        while True:
            try:
                if self.readContin:
                    s = port.readline()
                    if bool(s):
                        self.readUpdate = not self.readUpdate
                        print(s)
                        self.accumulatedMass += self.summ(s)
                        self.accumulatedMass = round(self.accumulatedMass, 2)
                    else:
                        continue
                else:
                    break
            except BaseException as exc:
                print(exc)

        port.close()
