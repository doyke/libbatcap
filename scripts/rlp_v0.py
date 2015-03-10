import serial

class ReLoadPro:
    ser= None
    def __init__(self,  portName):
        self.ser =  serial.Serial(portName, 115200,serial.EIGHTBITS, serial.PARITY_NONE , serial.STOPBITS_ONE)



print "Opening RLP Connection"
def_port = "/dev/ttyUSB1"
rlp = ReLoadPro(def_port) 
rlp.ser.write("read\n")
print rlp.ser.readline()
print "Closing RLP Connection"
rlp.ser.close()
