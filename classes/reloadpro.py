import serial

class ReLoadPro:
    ser= None
    def __init__(self,  portName):
        self.ser =  serial.Serial(portName, 115200,serial.EIGHTBITS, serial.PARITY_NONE , serial.STOPBITS_ONE)
        return self.ser
