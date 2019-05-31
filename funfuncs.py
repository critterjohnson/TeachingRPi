# funfuncs.py - fun methods for GPIO interaction
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
import shelve


# sets up the pi for GPIO output and creates the storage shelf
def start():
	GPIO.setmode(GPIO.BCM)
	# creates/clears the shelf object
	pins = shelve.open("pins")
	pins["in"] = {}
	pins["out"] = {}
	pins.close()

# cleans up and turns off everything that isn't off
def end():
	turn_off()
	GPIO.cleanup()

# waits a specified amount of time
def wait(sec):
	time.sleep(sec)

# sets up a pin for output and adds it to the shelf
def set_as_output(pin, name=None):
	pins = shelve.open("pins")
	pins["out"][pin] = pin
	if name is not None:
		pins["out"][name] = pin
	pins.close()
	GPIO.setup(pin, GPIO.OUT)

# sets a pin as input and adds it to the shelf
def set_as_input(pin, name=None):
	pins = shelve.open("pins")
	pins["in"][name] = pin
	if name is not None:
		pins["in"][name] = pin
	pins.close()
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# turns on a pin or pins by pin number or by name,
# or pass nothing to turn on all lights
def turn_on(*args):
	pins = shelve.open("pins")
	# turns on all lights if no arguments passed
	if len(args) == 0:
		for name, pin in pins["out"].items():
			GPIO.output(pin, True)
		print("no args")
	# get the pin numbers from the args
	else:
		for name in args:
			print("args")
			GPIO.output(pins[name], True)
	pins.close()

# turns off a pin or pins by pin number or name,
# or pass nothing to turn off all lights
def turn_off(*args):
	pins = shelve.open("pins")
	# turns on all lights if no arguments passed
	if len(args) == 0:
		for name, pin in pins["out"].items():
			GPIO.output(pin, False)
	# get the pin numbers from the args
	else:
		for name in args:
			GPIO.output(pins[name], False)
	pins = shelve.open("pins")
