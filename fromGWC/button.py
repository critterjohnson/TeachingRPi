import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(10) == 1:
            print("Pushed")
except KeyboardInterrjupt:
    GPIO.cleanup()

    
