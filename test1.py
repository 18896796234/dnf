import time

from foo.common import ch9329
from foo import huoquzuobiao


mykey = ch9329.kk
#ser = serial.Serial('COM3',baudrate=9600,timeout=0.2)

time.sleep(2)

mykey.keyDown('up')


time.sleep(2)

mykey.keyUp('up')
time.sleep(2)

mykey.keyDown('down')


time.sleep(2)

mykey.keyUp('down')
