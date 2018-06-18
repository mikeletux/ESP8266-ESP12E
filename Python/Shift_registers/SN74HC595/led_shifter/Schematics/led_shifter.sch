EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:switches
LIBS:relays
LIBS:motors
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:led_shifter-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L LED D7
U 1 1 5B2812EB
P 2400 2650
F 0 "D7" H 2400 2750 50  0000 C CNN
F 1 "LED" H 2400 2550 50  0000 C CNN
F 2 "" H 2400 2650 50  0001 C CNN
F 3 "" H 2400 2650 50  0001 C CNN
	1    2400 2650
	0    -1   -1   0   
$EndComp
$Comp
L LED D6
U 1 1 5B28147D
P 2700 2650
F 0 "D6" H 2700 2750 50  0000 C CNN
F 1 "LED" H 2700 2550 50  0000 C CNN
F 2 "" H 2700 2650 50  0001 C CNN
F 3 "" H 2700 2650 50  0001 C CNN
	1    2700 2650
	0    -1   -1   0   
$EndComp
$Comp
L LED D5
U 1 1 5B2814BA
P 3000 2650
F 0 "D5" H 3000 2750 50  0000 C CNN
F 1 "LED" H 3000 2550 50  0000 C CNN
F 2 "" H 3000 2650 50  0001 C CNN
F 3 "" H 3000 2650 50  0001 C CNN
	1    3000 2650
	0    -1   -1   0   
$EndComp
$Comp
L LED D4
U 1 1 5B2814EA
P 3300 2650
F 0 "D4" H 3300 2750 50  0000 C CNN
F 1 "LED" H 3300 2550 50  0000 C CNN
F 2 "" H 3300 2650 50  0001 C CNN
F 3 "" H 3300 2650 50  0001 C CNN
	1    3300 2650
	0    -1   -1   0   
$EndComp
$Comp
L LED D3
U 1 1 5B2816B6
P 3600 2650
F 0 "D3" H 3600 2750 50  0000 C CNN
F 1 "LED" H 3600 2550 50  0000 C CNN
F 2 "" H 3600 2650 50  0001 C CNN
F 3 "" H 3600 2650 50  0001 C CNN
	1    3600 2650
	0    -1   -1   0   
$EndComp
$Comp
L LED D2
U 1 1 5B2816BC
P 3900 2650
F 0 "D2" H 3900 2750 50  0000 C CNN
F 1 "LED" H 3900 2550 50  0000 C CNN
F 2 "" H 3900 2650 50  0001 C CNN
F 3 "" H 3900 2650 50  0001 C CNN
	1    3900 2650
	0    -1   -1   0   
$EndComp
$Comp
L LED D1
U 1 1 5B2816C2
P 4200 2650
F 0 "D1" H 4200 2750 50  0000 C CNN
F 1 "LED" H 4200 2550 50  0000 C CNN
F 2 "" H 4200 2650 50  0001 C CNN
F 3 "" H 4200 2650 50  0001 C CNN
	1    4200 2650
	0    -1   -1   0   
$EndComp
$Comp
L LED D0
U 1 1 5B2816C8
P 4500 2650
F 0 "D0" H 4500 2750 50  0000 C CNN
F 1 "LED" H 4500 2550 50  0000 C CNN
F 2 "" H 4500 2650 50  0001 C CNN
F 3 "" H 4500 2650 50  0001 C CNN
	1    4500 2650
	0    -1   -1   0   
$EndComp
$Comp
L R R0
U 1 1 5B281A8B
P 4500 3150
F 0 "R0" V 4580 3150 50  0000 C CNN
F 1 "100" V 4500 3150 50  0000 C CNN
F 2 "" V 4430 3150 50  0001 C CNN
F 3 "" H 4500 3150 50  0001 C CNN
	1    4500 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 3000 2400 2800
Wire Wire Line
	2700 3000 2700 2800
Wire Wire Line
	3000 3000 3000 2800
Wire Wire Line
	3300 3000 3300 2800
Wire Wire Line
	3600 3000 3600 2800
Wire Wire Line
	3900 3000 3900 2800
Wire Wire Line
	4500 3000 4500 2800
$Comp
L R R2
U 1 1 5B282064
P 3900 3150
F 0 "R2" V 3980 3150 50  0000 C CNN
F 1 "100" V 3900 3150 50  0000 C CNN
F 2 "" V 3830 3150 50  0001 C CNN
F 3 "" H 3900 3150 50  0001 C CNN
	1    3900 3150
	1    0    0    -1  
$EndComp
$Comp
L R R1
U 1 1 5B28213E
P 4200 3150
F 0 "R1" V 4280 3150 50  0000 C CNN
F 1 "100" V 4200 3150 50  0000 C CNN
F 2 "" V 4130 3150 50  0001 C CNN
F 3 "" H 4200 3150 50  0001 C CNN
	1    4200 3150
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 5B282219
P 3600 3150
F 0 "R3" V 3680 3150 50  0000 C CNN
F 1 "100" V 3600 3150 50  0000 C CNN
F 2 "" V 3530 3150 50  0001 C CNN
F 3 "" H 3600 3150 50  0001 C CNN
	1    3600 3150
	1    0    0    -1  
$EndComp
$Comp
L R R5
U 1 1 5B282222
P 3000 3150
F 0 "R5" V 3080 3150 50  0000 C CNN
F 1 "100" V 3000 3150 50  0000 C CNN
F 2 "" V 2930 3150 50  0001 C CNN
F 3 "" H 3000 3150 50  0001 C CNN
	1    3000 3150
	1    0    0    -1  
$EndComp
$Comp
L R R4
U 1 1 5B282229
P 3300 3150
F 0 "R4" V 3380 3150 50  0000 C CNN
F 1 "100" V 3300 3150 50  0000 C CNN
F 2 "" V 3230 3150 50  0001 C CNN
F 3 "" H 3300 3150 50  0001 C CNN
	1    3300 3150
	1    0    0    -1  
$EndComp
$Comp
L R R7
U 1 1 5B2822BF
P 2400 3150
F 0 "R7" V 2480 3150 50  0000 C CNN
F 1 "100" V 2400 3150 50  0000 C CNN
F 2 "" V 2330 3150 50  0001 C CNN
F 3 "" H 2400 3150 50  0001 C CNN
	1    2400 3150
	1    0    0    -1  
$EndComp
$Comp
L R R6
U 1 1 5B2822C6
P 2700 3150
F 0 "R6" V 2780 3150 50  0000 C CNN
F 1 "100" V 2700 3150 50  0000 C CNN
F 2 "" V 2630 3150 50  0001 C CNN
F 3 "" H 2700 3150 50  0001 C CNN
	1    2700 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4200 2800 4200 3000
$Comp
L GND #PWR?
U 1 1 5B282A85
P 2400 3300
F 0 "#PWR?" H 2400 3050 50  0001 C CNN
F 1 "GND" H 2400 3150 50  0000 C CNN
F 2 "" H 2400 3300 50  0001 C CNN
F 3 "" H 2400 3300 50  0001 C CNN
	1    2400 3300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5B282AB9
P 2700 3300
F 0 "#PWR?" H 2700 3050 50  0001 C CNN
F 1 "GND" H 2700 3150 50  0000 C CNN
F 2 "" H 2700 3300 50  0001 C CNN
F 3 "" H 2700 3300 50  0001 C CNN
	1    2700 3300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5B282AED
P 3000 3300
F 0 "#PWR?" H 3000 3050 50  0001 C CNN
F 1 "GND" H 3000 3150 50  0000 C CNN
F 2 "" H 3000 3300 50  0001 C CNN
F 3 "" H 3000 3300 50  0001 C CNN
	1    3000 3300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5B282B21
P 3300 3300
F 0 "#PWR?" H 3300 3050 50  0001 C CNN
F 1 "GND" H 3300 3150 50  0000 C CNN
F 2 "" H 3300 3300 50  0001 C CNN
F 3 "" H 3300 3300 50  0001 C CNN
	1    3300 3300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5B282B55
P 3600 3300
F 0 "#PWR?" H 3600 3050 50  0001 C CNN
F 1 "GND" H 3600 3150 50  0000 C CNN
F 2 "" H 3600 3300 50  0001 C CNN
F 3 "" H 3600 3300 50  0001 C CNN
	1    3600 3300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5B282B89
P 3900 3300
F 0 "#PWR?" H 3900 3050 50  0001 C CNN
F 1 "GND" H 3900 3150 50  0000 C CNN
F 2 "" H 3900 3300 50  0001 C CNN
F 3 "" H 3900 3300 50  0001 C CNN
	1    3900 3300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5B282BBD
P 4200 3300
F 0 "#PWR?" H 4200 3050 50  0001 C CNN
F 1 "GND" H 4200 3150 50  0000 C CNN
F 2 "" H 4200 3300 50  0001 C CNN
F 3 "" H 4200 3300 50  0001 C CNN
	1    4200 3300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5B282BF1
P 4500 3300
F 0 "#PWR?" H 4500 3050 50  0001 C CNN
F 1 "GND" H 4500 3150 50  0000 C CNN
F 2 "" H 4500 3300 50  0001 C CNN
F 3 "" H 4500 3300 50  0001 C CNN
	1    4500 3300
	1    0    0    -1  
$EndComp
$EndSCHEMATC
