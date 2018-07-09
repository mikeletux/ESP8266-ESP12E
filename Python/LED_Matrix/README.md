# LED MATRIX Project

Displays messages on a 1088bs led matrix screen dragging the text from left to right. Screen height must be 8 leds but width can be 8*N (being N the number of 1088bs modules) [ONLY 1 MODULE HAS BEEN TESTED]

### Components used
  - 2*SN74HC595 -> For column input and multiplexing columns.
  - 1088bs -> LED Matrix
  - mps2222a transistor -> For switching on and off the different 1088bs columns
  - Resistors -> According to my math (please check the electrinocs diagram for values)
  
4mA go through each lead when on. Since they are being multiplexed, to get more brightness we could go for 8mA.
