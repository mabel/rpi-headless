import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import os

row = 0
col = 0

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(3, GPIO.OUT) # set a port/pin as an output   
GPIO.output(3, 0)
GPIO.setup(5, GPIO.OUT) # set a port/pin as an output   
GPIO.output(5, 0)
GPIO.setup(7, GPIO.OUT) # set a port/pin as an output   
GPIO.output(7, 0)
GPIO.setup(8, GPIO.OUT) # set a port/pin as an output   
GPIO.output(8, 0)

def check_row_col(rc):
    print(rc)
    if rc == 41:
        os.system('mpc toggle')
        time.sleep(1)
        return
    if rc == 43:
        os.system('mpc next')
        time.sleep(1)
        return
    os.system("mpc stop; sleep 1; mpc clear; sleep 1; mpc load " + str(rc) + "; mpc shuffle; mpc play")
    time.sleep(1)

while True:
    time.sleep(0.1)
    col = 0
    row = 10
    GPIO.output(3, 1)
    if GPIO.input(11) == GPIO.HIGH:
        col = 1
    if GPIO.input(13) == GPIO.HIGH:
        col = 2
    if GPIO.input(15) == GPIO.HIGH:
        col = 3
    GPIO.output(3, 0)
    if col > 0:
        check_row_col(row + col)
        continue
    row = 20
    GPIO.output(5, 1)
    if GPIO.input(11) == GPIO.HIGH:
        col = 1
    if GPIO.input(13) == GPIO.HIGH:
        col = 2
    if GPIO.input(15) == GPIO.HIGH:
        col = 3
    GPIO.output(5, 0)
    if col > 0:
        check_row_col(row + col)
        continue
    row = 30
    GPIO.output(7, 1)
    if GPIO.input(11) == GPIO.HIGH:
        col = 1
    if GPIO.input(13) == GPIO.HIGH:
        col = 2
    if GPIO.input(15) == GPIO.HIGH:
        col = 3
    time.sleep(0.1)
    GPIO.output(7, 0)
    if col > 0:
        check_row_col(row + col)
        continue
    row = 40
    GPIO.output(8, 1)
    if GPIO.input(11) == GPIO.HIGH:
        col = 1
    if GPIO.input(13) == GPIO.HIGH:
        col = 2
    if GPIO.input(15) == GPIO.HIGH:
        col = 3
    time.sleep(0.1)
    GPIO.output(8, 0)
    if col > 0:
        check_row_col(row + col)
        continue
