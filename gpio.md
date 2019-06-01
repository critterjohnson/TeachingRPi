# GPIO with the Pi
## What is GPIO?
GPIO stands for General Purpose Input-Output, and is used to send and receive electrical signals. 40 "pins" make up the GPIO on the raspberry pi, each with a 2 different numbers assigned to it. The "physical" number, or the number the pin is based on location, and the "Broadcom Pin Number", or "BCM". The "BCM" pin number is usually what you deal with on the Raspberry Pi. The numbers are assigned as follows (credit to [pinout.xyz](https://pinout.xyz)):
![rpi pinout](https://pinout.xyz/resources/raspberry-pi-pinout.png)
with the numbers above and below the pinout being the BCM numbers. Notice that not all pins are numbered: some pins, like physical pin 1, carry 3.3V; others, like physical pins 2 and 4, carry 5V. This is important because these pins always send a signal and are not controlled by the Pi, unlike the BCM numbered pins that only send a signal when told and can also be set up to receive signals.
## Breadboards with GPIO
Breadboards are boards with many pin holes used to connect electronics and build circuits. They work like this (credit to [thepihut.com](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins)):

![breadboard example](https://cdn.shopify.com/s/files/1/0176/3274/files/Breadboard_Remarked_grande.png?15033584625641436291)

Power (positive) is connected to one of the outermost red lines, and ground (negative) is connected to one of the outermost blue lines. This way, connections to power and ground can easily be made from any point on the board.
## GPIO with LEDs
Using an LED with GPIO is simple, as long as necessary precautions are taken. **First and foremost, a resistor must ALWAYS be used when connecting an LED to the Pi via GPIO. This is to ensure that the LED doesn't burn out the Pi or blow up the LED** (trust me, not as cool as it sounds, it doesn't even make a noise and smells terrible). Power to the LED comes from one of the numbered GPIO pins on the Pi, and goes to the positive (long) lead on the LED. The LED must be grounded to complete the circuit. The ground end is where the resistor should go before connecting to one of the blue ground lines on the breadboard. Note that the resistors run vertically (credit again to [thepihut.com](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins)):

![LED diagram](https://cdn.shopify.com/s/files/1/0176/3274/files/LEDs-BB400-1LED_bb_grande.png?6398700510979146820)

Disregard the connections to the Pi on the diagram, they are for an outdated model of Pi.
### GPIO with Buttons
Buttons with the Pi are different because power always flow *to* the button but cannot flow *through* the button to complete the circuit until the button is pressed. Luckily, GPIO pins can detect when they are receiving power too. While a resistor here isn't 100% necessary, it is recommended. Power comes from one of the sides of the Pi (on the T-Shaped canakit breakout boards, this should be the side that says 3V3); and ground goes into the Pi this time (credit to [raspberrypihq.com](https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/)):

![Button diagram](https://raspberrypihq.com/wp-content/uploads/2018/02/02_Push-button_bb-min-255x300.jpg)