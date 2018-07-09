from Screen import Screen
from FileHandler import FileHandler
import machine
from machine import Pin, SPI, Timer	
from array import array

def raiseFlag(t):
	global interruptFlag
	interruptFlag = True

WIDTH = 8
INTERRUPT_TIME = 50
interruptFlag = False

PIN_OE = 4
PIN_CS_ROW = 15
PIN_CS_COL = 5
FILENAME = 'message.txt'

hspi = SPI(1, baudrate=80000000, polarity=0, phase=0)
oe = Pin(PIN_OE,Pin.OUT)
cs_row = Pin(PIN_CS_ROW,Pin.OUT)
cs_col = Pin(PIN_CS_COL,Pin.OUT)

f =	FileHandler(FILENAME)

s = Screen(WIDTH, f.getMessageFromFile())
s.fromStringToHexBuffer()

dragTimer = Timer(0)
dragTimer.init(period=INTERRUPT_TIME, mode=Timer.PERIODIC, callback=raiseFlag)

i = 0
j = 0
col = 1
while True:
	while not interruptFlag:
		while i < s.width:
			cs_row.value(0)
			cs_col.value(0)
			hspi.write(bytearray([s.screen[i]]))
			oe.value(1)
			cs_row.value(1)
			hspi.write(bytearray([col]))
			cs_col.value(1)
			oe.value(0)
			i += 1
			col = col << 1
		i = 0
		col = 1
		j += 1
	s.crossScreenWithMessage()
	interruptFlag = False