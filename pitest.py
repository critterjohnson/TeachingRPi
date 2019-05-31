import RPi.GPIO as GPIO
from picamera import PiCamera
import time

led = 21
button = 26

def test_board():
	GPIO.setmode(GPIO.BCM)
	
	# tests lights
	GPIO.setup(led, GPIO.OUT)
	GPIO.output(led, True)
	time.sleep(2)
	GPIO.output(led, False)

	# tests the button
	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	while True:
		try:
			if GPIO.input(button):
				print("Button pressed: test passed")
				GPIO.cleanup()
				break
		except KeyboardInterrupt:
			print("Button not pressed: test failed")
			GPIO.cleanup()
			break

if __name__ == "__main__":
	test_board()
