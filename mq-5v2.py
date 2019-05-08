#!/usr/bin/env python
# -*- coding: utf-8 -*-
#the sensor has to be connected to pin 1 for power, pin 6 for ground
# and pin 7 for signal(board numbering!).

import time, sys
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.OUT)#Indicamos que el pin 11 será de salida
GPIO.output(11,True) #Indicamos que el pin 11 esta LOW (sin señal)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def actionMq5(pin):
	GPIO.output(11, False) #Enviamos la señal de activación al buzzer pin 7 HIGH
	time.sleep(1) #La señal (pitido) dura 5 segundos
	GPIO.output(11,True) #Cerramos la señal poniendo el pin 7 en LOW y el buzzer se calla.
	print('Sensor mq5 detected action!')
	return
def actionTermo(pin):
	for i in range(5):
		GPIO.output(11, False) #Enviamos la señal de activación al buzzer pin 7 HIGH
		time.sleep(0.1) #La señal (pitido) dura 5 segundos
		GPIO.output(11,True) #Cerramos la señal poniendo el pin 7 en LOW y el buzzer se calla.
		time.sleep(0.1)
		GPIO.output(11, False)
		time.sleep(0.1)
		GPIO.output(11,True)
	print('Sensor termo detected action!')
	return
	
	

GPIO.add_event_detect(7, GPIO.RISING)
GPIO.add_event_callback(7, actionMq5)
GPIO.add_event_detect(13, GPIO.RISING)
GPIO.add_event_callback(13, actionTermo)

try:
    while True:
        print('alive')
        time.sleep(1)
			
			
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
