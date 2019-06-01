# TeachingRPi
#### with some code from https://github.com/KsMomOf2/GWCRaspberryPi

## About
I wrote this code to teach middle schoolers about raspberry pi's and GPIO, with a little Python mixed in there.

## Methods
All additional methods are added to funfuncs.py

### start
```python
def start()
```
sets up the pi for GPIO output on BCM and creates the persitent shelve object

### end
```python
def end()
```
cleans up and turns off everything that isn't off

### wait
```python
def wait(sec)
```
waits 'sec' seconds; time.sleep(sec)

### set_as_output
```python
def set_as_output(pin, name=None)
```
sets 'pin' as an output pin by number and adds it to the persistent storage shelf

additionally can be named using the 'name' parameter 

### set_as_input
```python
def set_as_output(pin, name=None)
```
sets 'pin' as an output pin by number and adds it to the persistent storage shelf

additionally can be named using the 'name' parameter 

### turn_on
```python
def turn_on(*args)
```
turns on all lights passed in args by pin number or name (as passed to set_as_input)

if nothing is passed, turns on all lights

### turn_off
```python
def turn_off(*args)
```
turns off all lights passed in args by pin number or name (as passed to set_as_input)

if nothing is passed, turns off all lights

### wait_for
```python
def wait_for(*args, **kwargs)
```
waits for a button or buttons passed to args by pin number or name (as passed to set_as_output)

if nothing is passed, waits for all buttons

if passed 
```python 
mode="and"
``` 
waits for all buttons to be pressed

if passed 

```python 
mode="or"
``` 
waits for only one button to be pressed

### cam_preview
```python
def cam_preview(sec=10)
```
shows what the camera is seeing for "sec" seconds

### cam
```python
def cam(file_name, timer=2)
```
takes a picture and saves it to (current working directory)/file_name.jpg

if timer > 2, timer is set to 2 (camera needs at least 2 seconds for the light sensors)

## Using funfuncs.py
Start by importing the funfuncs methods and setting up the board:
```python
from funfuncs import *

start()
```
**Note: In general, import * is not recommended. However, funfuncs.py only contains a few methods, all of which will most likely be used.**

After starting, adding pins as input and output pins is required to use the other funfuncs methods.

For output devices (lights):
```python
set_as_output(pin)
```
Optionally, pins can be named:
```python
set_as_output(pin, "light1")
set_as_output(pin2, "light2")
```
For input devices (buttons):
```python
set_as_input(pin)
```
These can also be named:
```python
set_as_input(pin, "button1")
set_as_input(pin2, "button2")
```
Lights can be turned on using turn_on:
```python
turn_on()
```
If no arguments are put in the parentheses, all of the lights will be turned on. The same is true for turn_off:
```python
turn_off()
```
However, both of these methods can take individual pin numbers or names to turn on and off:
```python
turn_on("light1", "light2")
wait(3)
turn_off("light1")
wait(3)
turn_off("light2")
```
For buttons, we have the wait_for function, which will wait to continue the program until a button is pressed.
```python
wait_for()
turn_on("light1")
wait(0.5)
turn_off("light1")
```
The wait_for function can also either take button names/pin numbers or not. Without names/numbers it waits for all buttons, with pin numbers/buttons it waits for certain buttons. The wait_for function has two different modes: "and" mode, which waits for all buttons to be pressed (default), as well as "or" mode, which waits for any one button to be pressed of the list of buttons it is given. You can specify the modes by passing mode="and" or mode="or":
```python
# and mode:
wait_for("button1", mode="and")
# or mode:
wait_for("button1", mode="or")
```
funfuncs also has functions to interact with the camera.