import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

def blink(times):
  for i in range (0,times):
    GPIO.output(18, GPIO.HIGH)
    print("on")
    print("value of i:",i)
    time.sleep(2)
    GPIO.output(18, GPIO.LOW)
    print("off")
    time.sleep(1)

blink(10)
print("before cleanup")
GPIO.cleanup()
print("after cleanup")

