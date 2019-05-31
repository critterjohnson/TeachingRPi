# get some fun functions
from funfuncs import *

start()
# --- your code below ---

set_as_input(26, "cat")
set_as_output(21, "dog")

count = 0
while count < 10:
	wait_for("cat", mode="and")
	count += 1
	turn_on("dog")
	wait(0.1)
	turn_off()

# --- *************** ---
end()
