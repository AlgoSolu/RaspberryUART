import collections
import serial
from constant import *
RX = collections.namedtuple('RX',['status','type','lamp','value','unit'])
env = dev_or_prod()

class uart:
    def __init__(self):
        self.connect()

    def connect(self):
        try:
            self.uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)
            serial.PARITY_NONE
            serial.EIGHTBITS
            serial.STOPBITS_ONE
            self.Status = 1
            self.uart.flushInput()
            self.uart.timeout=None
            print('UART init success')
        except Exception as e:
            print(e)
            self.Status = 0
            
    def readlineCR(self):
        try:
            if self.Status == 2:
                self.connect()
                
            elif self.Status == 1:
                self.uart.write('D'.encode());
                if DEBUG:
                    print("D sended:")
                
                line = []
                for c in self.uart.readline():
                    if env == "prod":
                        line.append(ord(c))   # Make sure 'c' is ASCII integer value
                    else:
                        line.append(c)
                    if c == 10 or c == '\n':
                        l = len(line)
                        if l > 2:
                            status = ''.join(chr(ch) for ch in line[0:2])
                            type   = ''.join(chr(ch) for ch in line[3:5])
                            lamp   = ''.join(chr(ch) for ch in line[6:8])
                            value  = float(''.join(chr(ch) for ch in line[10:17]))
                            unit   = ''.join(chr(ch) for ch in line[18:20])
                            
                            if DEBUG:
                                print(line)
                                print("Status: ", status)
                                print("Type:   ", type)
                                print("Lamp:   ", lamp)
                                print("Value:  ", value)
                                print("Unit:   ", unit)
                            
                            return RX(status,type,lamp,value,unit);
        except Exception as e:
            print(e)
            self.Status = 2
            connect()