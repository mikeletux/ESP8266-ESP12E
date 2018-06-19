######################################################
# Example of using timers on ESP8266                 #
# Original code taken from http://www.srccodes.com   #
######################################################

from machine import Timer, Pin
import time
 
#Define a function to blink a LED
def blink(led):
     led.value(not led.value())
 
#Setup a GPIO pin for output
myLed = Pin(16, Pin.OUT)
myLed2 = Pin(5, Pin.OUT)
#Construct a virtual (id=-1) timer
blinkTimer = Timer(0)
blinkTimer2 = Timer(1)
#Setup the timer to call the custom blink function at a regular interval of 0.5 second
blinkTimer.init(period=500, mode=Timer.PERIODIC, callback=lambda t:blink(myLed))
blinkTimer2.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:blink(myLed2))
#Wait
time.sleep_ms(10000)
#Switch off the LED
myLed.value(0)
myLed2.value(0)
#deinitialize/stop the timer
blinkTimer.deinit()
blinkTimer2.deinit()