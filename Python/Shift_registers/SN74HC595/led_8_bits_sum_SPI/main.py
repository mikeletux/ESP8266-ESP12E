#################################################
# SN74HC595 with software SPI ESP12-E           #
# Sums up 1 bit by 1 bit till 255 is reached    #
# Author: Miguel Sama                           #
# Date: 19/06/2018                              #
#################################################

from machine import Pin, SPI
import utime

#Software SCLK at PIN 0 (D3 dev board)
#Software MOSI at PIN 2 (D4 dev board)
#Used PIN 15 (D8 dev board) as latch
#~OE connected directly to GND
#~SRCLR connected directly to VCC
#LSB LED connected to Qa. MSB LED connected to Qh

latch = Pin(15,Pin.OUT)
spi = SPI(-1, baudrate=200000, polarity=0, phase=0, sck=Pin(0), mosi=Pin(2), miso=Pin(4))

a = 0
while True:
	while a < 256:
		latch.value(0)
		spi.write(bytearray([a]))
		latch.value(1)
		a += 1
		utime.sleep_ms(50)
	a = 0
	
	