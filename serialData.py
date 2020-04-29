import serial
import serial.tools.list_ports as serialPorts
from time import sleep
import re


class portScales:
    accumulatedMass = 0
    lastMass = 0
    number = 0
    portsNames = None
    readContin = False
    readUpdate = False
    zeroing = False

    def __init__(self):
        self.portsNames = self.portDiscovery()

    def stopRead(self):
        self.readContin = False

    def startRead(self):
        self.readContin = True

    def summ(self, newWeight):
        pattern = re.compile('\d{2}.\d{2}')
        result = re.search(pattern, newWeight.decode('ascii'))
        return float(result.group(0))

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
                        print(s)
                        self.lastMass = self.summ(s)
                        self.accumulatedMass += self.lastMass
                        self.number += 4
                        self.accumulatedMass = round(self.accumulatedMass, 2)
                        sleep(0.1)
                        self.readUpdate = not self.readUpdate
                    else:
                        continue
                else:
                    break
            except BaseException as exc:
                print(exc)

        port.close()
