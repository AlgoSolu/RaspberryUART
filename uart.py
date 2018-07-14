import collections
import serial
from constant import *
RX = collections.namedtuple('RX',['status','type','lamp','value','unit'])

class uart:
    def __init__(self):
        ##################
        # UART interface #
        ##################
        try:
            self.uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)
            serial.PARITY_NONE
            serial.EIGHTBITS
            serial.STOPBITS_ONE
            self.Status = 1
        except:
            self.Status = 0
            print("Cannot open port")
    def readlineCR(self):
        if self.Status == 1:
            self.uart.write('D'.encode());
            line = []
            while True:
                for c in self.uart.readline():
                    line.append(c)
                    if c == 10:
                        l = len(line)
                        if l > 2:
                            if line[l-2] == 13:
                                status = ''.join(chr(ch) for ch in line[0:2])
                                type   = ''.join(chr(ch) for ch in line[3:5])
                                lamp   = ''.join(chr(ch) for ch in line[6:8])
                                value  = float(''.join(chr(ch) for ch in line[9:17]))
                                unit   = ''.join(chr(ch) for ch in line[18:20])

                                if DEBUG:
                                    #print("Line: " + ''.join(str(line)))
                                    print("Line: " + ''.join(chr(ch) for ch in line))
                                    print("Status: ", status)
                                    print("Type:   ", type)
                                    print("Lamp:   ", lamp)
                                    print("Value:  ", value)
                                    print("Unit:   ", unit)

                            return RX(status,type,lamp,value,unit);
