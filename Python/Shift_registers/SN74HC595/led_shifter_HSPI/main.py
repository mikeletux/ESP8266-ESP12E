############################################
# SN74HC595 with hardware SPI ESP12-E      #
# Simple 8 LED shifter proof of concept    #
# Author: Miguel Sama                      #
# Date: 18/06/2018                         #
############################################

from machine import Pin, SPI
import utime

#Hardware SCLK at PIN 14 (D5 dev board)
#Hardware MOSI at PIN 13 (D7 dev board)
#Used PIN 15 (D8 dev board) as latch
#~OE connected directly to GND
#~SRCLR connected directly to VCC
#LSB LED connected to Qa. MSB LED connected to Qh

latch = Pin(15,Pin.OUT)
hspi = SPI(1, baudrate=10000000, polarity=0, phase=0)

a = 1
while True:
	while a < 256:
		latch.value(0)
		hspi.write(bytearray([a]))
		latch.value(1)
		a = a << 1
		#utime.sleep_ms(2)
	a = 1
	
	