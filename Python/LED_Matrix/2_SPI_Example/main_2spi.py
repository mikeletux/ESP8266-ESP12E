from Screen import Screen
import machine
from machine import Pin, SPI, Timer	
from array import array

def raiseFlag(t):
	global interruptFlag
	interruptFlag = True

WIDTH = 8
INTERRUPT_TIME = 50
interruptFlag = False

latch = Pin(15,Pin.OUT)
hspi = SPI(1, baudrate=1000000, polarity=0, phase=0)
spi = SPI(-1, baudrate=1000000, polarity=0, phase=0, sck=Pin(5), mosi=Pin(4), miso=Pin(0)) #Maybe with only one SPI can be done...

s = Screen(WIDTH, "Hello World!")
s.fromStringToHexBuffer()

dragTimer = Timer(0)
dragTimer.init(period=INTERRUPT_TIME, mode=Timer.PERIODIC, callback=raiseFlag)

i = 0
j = 0
col = 1
while True:
	while not interruptFlag:
		while i < s.width:
			latch.value(0)
			hspi.write(bytearray([s.screen[i]]))
			spi.write(bytearray([col]))
			latch.value(1)
			i += 1
			col = col << 1
		i = 0
		col = 1
		j += 1
	s.crossScreenWithMessage()
	interruptFlag = False