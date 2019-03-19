#!/usr/bin/env python3
import RPi.GPIO as GPIO
from pynput.keyboard import Key, Controller
import subprocess
import time


channels = {16: False}
keyboard = Controller()
pin = 16
RUNNING = False


def execute(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)


def event_callback(channel):
    global RUNNING
    global execute

    msg = 'Employee connected.\n\n from: "Moscone Center"\n Terminal: MiMo-{0}\n\n'.format(channel)
    print(msg)

    if not channels[channel] and GPIO.input(pin) and RUNNING is False:
        print('Starting up...\n\n')
        
        try:
            execute('/home/pi/M-OS/app.sh')
            RUNNING = True
        except Exception as e:
            print(e)
        
        channels[channel] = not channels[channel]

        # Turn on screen
        execute('/usr/bin/xset dpms force on')

    else:
        print('Shutting down...\n\n')

        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        channels[channel] = not channels[channel]
        RUNNING = False
        
        # Turn off screen
        execute('/usr/bin/xset dpms force off')

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(pin, GPIO.BOTH, callback=event_callback, bouncetime=1000)

def main():
    print('Waiting for cables...\n\n')
    while True:
        time.sleep(.1)


if __name__ == '__main__':
    # Shutdown screen
    command = '/usr/bin/xset dpms force off'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    main()
