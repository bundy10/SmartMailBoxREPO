import RPi.GPIO as GPIO

import threading, time

import logging

from picamera import PiCamera

from time import sleep


logging.basicConfig(level=logging.DEBUG)

GPIO.setmode(GPIO.BCM)



class LED:
	
	channel = 0

	def __init__(self, channel):
		
		self.channel = channel

		GPIO.setup(self.channel, GPIO.OUT)

	def on(self):
		
		GPIO.output(self.channel, GPIO.HIGH)

		return "on"

	def off(self):

		GPIO.output(self.channel, GPIO.LOW)

		return "off"

class States:
    

    def state1():
        running = True
        while(running):
            global state
            state = 1
            GPIO.setup(10, GPIO.OUT)
            #state waiting for delivery
            while state == 1:
                if GPIO.input(8) == 0:
                    GPIO.output(10, GPIO.HIGH)

    def state2():
        global state
        state = 2
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(2, GPIO.OUT)
        GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        #state waiting for user to unlock
        GPIO.output(10, GPIO.LOW)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(2, GPIO.LOW)
        yo = False
        while yo == False:
            if GPIO.input(21) == 1:
                state = 3
                States.state3()
    
    def state3():
        #state while door is open
        global state
        state = 3
        GPIO.output(5, GPIO.LOW)
        while state == 3:
            print("door open")
            if GPIO.input(21) == 0:
                state = 4
                States.state4()

    def state4():
            GPIO.setup(3, GPIO.OUT)
            #state triggered by door closing
            #takes photo
            print("locked")
            GPIO.output(2, GPIO.HIGH)
            GPIO.output(3, GPIO.HIGH)
            camera = PiCamera()
            camera.start_preview()
            time.sleep(3)
            camera.capture('/home/mailbox/Pictures/image.jpg')
            camera.stop_preview()
            camera.close()
            time.sleep(3)
            GPIO.output(3, GPIO.LOW)
            global state
            state = 1

class Switch:

	def __init__(self, channel):
		
		self.channel = channel

		GPIO.setup(self.channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	def isTriggered(self):
		
		return GPIO.input(self.channel)






class Camera:

	def TakePhoto():

		GPIO.setup(10, GPIO.OUT)
		camera.start_preview() #turn camera on
		GPIO.output(10, GPIO.HIGH)
		time.sleep(5) #give it time to adjust to light level
		camera.capture('/home/pi/Desktop/image.jpg')
		camera.stop_preview()
		GPIO.output(10, GPIO.LOW)

		