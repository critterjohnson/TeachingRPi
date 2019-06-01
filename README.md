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