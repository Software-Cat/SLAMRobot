import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

motor = 16

GPIO.setup(motor, GPIO.OUT)

print("turning motor on")
GPIO.output(motor,GPIO.high)

sleep(2)

print("stopping motor")
GPIO.output(motor,GPIO.LOW)

GPIO.cleanup()
