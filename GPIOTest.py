# Get the libraries you need
import RPi.GPIO as GPIO
from picamera import PiCamera
import time

# Define the pins.  If you set up your hardware on different pins, change the numbers here
red = 21
green = 22
yellow = 27
button = 23
buzzer = 19
motion = 12

# Sets up the three lights for the traffic light
def setup():
    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(green, GPIO.OUT)
    GPIO.setup(yellow, GPIO.OUT)

# Turns on all three of the lights for traffic light
def allOn():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(red, True)
    GPIO.output(green, True)
    GPIO.output(yellow, True)

# Turns off all three of the lights for traffic light
def allOff():
    GPIO.output(red, False)
    GPIO.output(green, False)
    GPIO.output(yellow, False)

# Run a traffic light, Setup the lights, turn them on, wait, turn them off, then
# run a loop that turns the red on, then the red off and the green on, then the green
# off and the yellow on, then the yellow off
def trafficLight(times):
    setup()
    allOn()
    time.sleep(2)
    allOff()
    for num in range(1,times):    
        GPIO.output(red,True)
        time.sleep(2)
        GPIO.output(red, False)
        GPIO.output(green, True)
        time.sleep(2)
        GPIO.output(green, False)
        GPIO.output(yellow, True)
        time.sleep(1)
        GPIO.output(yellow, False)

# Demonstrates the use of a push button.  You may need to experiment with the setup,
#       I provided 3 setup commands that all work a little differently based on whether you
#       choose to react to True or to False
# With a button, you normally want to keep track of whether the button is on or off
#     which requires a boolean variable, see btnOn below
#This turns the red light on/off when you push the button

def pressLight():
    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#    GPIO.setup(button, GPIO.IN)
    press = 10
    count = 0
    btnOn = False
    while count < press:
        btn = GPIO.input(button)
        #if btn:
            #print("Nothing")
        #else:
        if not btn:
            count = count + 1
            if btnOn:
                print("Low")
                GPIO.output(red, GPIO.LOW)
                btnOn = False
                time.sleep(1)
            else:
                print("High")
                GPIO.output(red, GPIO.HIGH)
                btnOn = True
        time.sleep(.05)

#The buzzer is the simplest of the circuits as it needs no resistor.  Just positive and negative
# You us High to make the sound and Low to turn it off

def buzz():
    GPIO.setup(buzzer, GPIO.OUT)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(buzzer, GPIO.LOW)

#This uses the motion detector and prints out that motion was detected
# The connection is a little different as there are three wires:
# red - power (5V), black - ground, and then the pin to check - green
def movement(times):
    GPIO.setup(motion, GPIO.IN)
    time.sleep(2) # Let motion pir settle after program started
    count = 0
    while count < times:
        if GPIO.input(motion):
            print("Motion Detected!")
            count = count + 1
            time.sleep(2) # Delay to avoid multiple detection
        time.sleep(0.1)

# This will test an output pin
def testOut(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)
    time.sleep(2)

# This will test an input pin
def testIn(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    while True:
        try:
            if GPIO.input(pin):
                print("Button")
                time.sleep(0.2)
        except KeyboardInterrupt:
            GPIO.cleanup()
            break
        
def cam_preview(sec):
    camera = PiCamera()
    camera.start_preview()
    time.sleep(sec)
    camera.stop_preview()

def cam(save_location):
    camera = PiCamera()
    camera.start_preview()
    time.sleep(2)
    try:
        camera.capture(save_location)
    except:
        pass
    camera.stop_preview()

def main():
    #GPIO.setmode(GPIO.BCM)
    #setup()

    #trafficLight(3)
    #pressLight()
    #buzz()
    #movement(4)
    #testIn(motion)
    #testOut(buzzer)

    GPIO.setmode(GPIO.BCM)
    setup()
    allOn()
    time.sleep(2)
    allOff()
    GPIO.cleanup()

    #testIn(26)
    #testIn(19)

    #cam_preview(10)
    #cam("/home/pi/Desktop/TeachingRPi/img.jpg")

main()

