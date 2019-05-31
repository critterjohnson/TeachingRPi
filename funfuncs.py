# funfuncs.py - fun methods for GPIO interaction
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
import shelve


# sets up the pi for GPIO output and creates the storage shelf
def start():
	GPIO.setmode(GPIO.BCM)
	# creates/clears the shelf object
	with shelve.open("pins") as pins:
		pins["in"] = {}
		pins["out"] = {}

# cleans up and turns off everything that isn't off
def end():
	turn_off()
	GPIO.cleanup()

# sets up a pin for output and adds it to the shelf
def set_as_output(pin, name=None):
	with shelve.open("pins") as pins:
		pins["out"][pin] = pin
		if name is not None:
			pins["out"][name] = pin
	GPIO.setup(pin, GPIO.OUT)

# sets a pin as input and adds it to the shelf
def set_as_input(pin, name=None):
	with shelve.open("pins") as pins:
		pins["in"][name] = pin
		if name is not None:
			pins["in"][name] = pin
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# turns on a pin or pins by pin number or by name,
# or pass nothing to turn on all lights
def turn_on(*args):
	# turns on all lights if no arguments passed
	if len(args) == 0:
		with shelve.open("pins") as pins:
			for name, pin in pins["out"].items():
				GPIO.output(pin, True)
	# get the pin numbers from the args
	else:
		with shelve.open("pins") as pins:
			for name in args:
				GPIO.output(pins[name], True)

# turns off a pin or pins by pin number or name,
# or pass nothing to turn off all lights
def turn_off(*args):
	# turns on all lights if no arguments passed
	if len(args) == 0:
		with shelve.open("pins") as pins:
			for name, pin in pins["out"].items():
				GPIO.output(pin, False)
	# get the pin numbers from the args
	else:
		with shelve.open("pins") as pins:
			for name in args:
				GPIO.output(pins[name], False)
