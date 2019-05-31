# get some fun functions
from funfuncs import *

start()

# set inputs and outputs
set_as_input(26, "button") # sets pin 26 as an input and names it "button"
set_as_output(21, "light") # sets pin 21 as an output and names it "light"

# demo GPIO
count = 0
while count < 10:
	wait_for("button", mode="and")
	count = count + 1
	print(count)
	turn_on("light")
	wait(0.2)
	turn_off()

# demo camera - note: Both tests cannot be run at once
cam_preview()
#print("Taking picture in 10 seconds...")
#cam("critter", 10)

end()