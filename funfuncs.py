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
	pins = shelve.open("pins", writeback=True)
	pins["out"][pin] = pin
	if name is not None:
		pins["out"][name] = pin
	pins.close()
	GPIO.setup(pin, GPIO.OUT)

# sets a pin as input and adds it to the shelf
def set_as_input(pin, name=None):
	pins = shelve.open("pins", writeback=True)
	pins["in"][name] = pin
	if name is not None:
		pins["in"][name] = pin
	pins.close()
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# turns on a pin or pins by pin number or by name,
# or pass nothing to turn on all lights
def turn_on(*args):
	pins = shelve.open("pins", writeback=True)
	# turns on all lights if no arguments passed
	if len(args) == 0:
		for name, pin in pins["out"].items():
			GPIO.output(pin, True)
	# get the pin numbers from the args
	else:
		for name in args:
			GPIO.output(pins[name], True)
	pins.close()

# turns off a pin or pins by pin number or name,
# or pass nothing to turn off all lights
def turn_off(*args):
	pins = shelve.open("pins", writeback=True)
	# turns on all lights if no arguments passed
	if len(args) == 0:
		for name, pin in pins["out"].items():
			GPIO.output(pin, False)
	# get the pin numbers from the args
	else:
		for name in args:
			GPIO.output(pins[name], False)
	pins = shelve.open("pins")

# waits for an input from a button multiple buttons 
# by pin number or name or pass nothing to wait for all buttons
# if mode is "and", waits for all buttons
# if mode is "or", waits for only one button
def wait_for(*args, **kwargs):
	# sets default params
	if "mode" in kwargs:
		mode = kwargs["mode"]
	else:
		mode = "and"
	pins = shelve.open("pins", writeback=True)
	# waits for all buttons if no arguments passed
	if len(args) == 0:
		print("no args")
		if mode == "or":
			print("or")
			print(pins["out"].items())
			pressed = False
			while not pressed:
				for name, pin in pins["out"].items():
					if GPIO.input(pin):
						print("got press")
						pressed = True
		elif mode == "and":
			# creates pin states dict
			pin_states = {}
			for name, pin in pins["out"].items():
				pin_states[pin] = False
			while True:
				# assigns pin states
				for name, pin in pins["out"].items():
					pin_states[pin] = GPIO.input(pin)
				# checks pin states
				count = 0
				for pin, val in pin_states.items():
					if val:
						count += 1
					else:
						break
				if count == len(pin_states):
					break
	# waits for certain buttons
	else:
		print("args")
		# waits for certain buttons if no arguments passed
		if mode == "or":
			print("or")
			pressed = False
			while not pressed:
				for name, pin in pins["out"].items():
					if name in args: # and GPIO.input(pin):
						print("got press")
						pressed = True
		elif mode == "and":
			# creates pin states dict
			pin_states = {}
			for name in args:
				pin_states[pins["out"][name]] = False
			while True:
				# assigns pin states
				for pin, val in pin_states:
					pin_states[pin] = GPIO.input(pin)
				# checks pin states
				count = 0
				for pin, val in pin_states.items():
					if val:
						count += 1
					else:
						break
				if cound == len(pin_states):
					break
	pins.close()
