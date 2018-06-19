#################################################
# SN74HC595 with hardware SPI ESP12-E           #
# Sums up 1 bit by 1 bit till 255 is reached    #
# Author: Miguel Sama                           #
# Date: 18/06/2018                              #
#################################################

from machine import Pin, SPI
import utime

#Hardware SCLK at PIN 14 (D5 dev board)
#Hardware MOSI at PIN 13 (D7 dev board)
#Used PIN 15 (D8 dev board) as latch
#~OE connected directly to GND
#~SRCLR connected directly to VCC
#LSB LED connected to Qa. MSB LED connected to Qh

latch = Pin(15,Pin.OUT)
hspi = SPI(1, baudrate=1000000, polarity=0, phase=0)

a = 0
while True:
	while a < 256:
		latch.value(0)
		hspi.write(bytearray([a]))
		latch.value(1)
		a += 1
		utime.sleep_ms(50)
	a = 0
	
	