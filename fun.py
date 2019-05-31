# get some fun functions
from funfuncs import *

start()
# --- your code below ---

set_as_input(26, "cat")
set_as_output(21, "dog")

while True:
	print("outermost while loop")
	wait_for("cat", mode="or")
	turn_on("dog")
	wait(0.1)
	turn_off()

# --- *************** ---
end()
