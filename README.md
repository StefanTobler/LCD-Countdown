# LCD-Countdown

This is a library to display a countdown to a certain eepoch time on a 16x2 LCD display using a Raspberry Pi. 

## How to use

Set the countdown time with the method `setEpoch(t)`, the `t` should be the epoch second of the date.
You can generate the epoch time at [Epoch Converter](https://www.epochconverter.com/).

**Note**: If the epoch time you set is less than the current epoch time an error will be thrown.

Next, use the `setText(message)` method to change the title of your countdown.

**Note**: `text` must be shorter than 16 characters

Finally run the `main()` method and the counutdown will begin.

## PIN OUT FOR LCD
| LCD | GPIO |
|-----|------|
| VSS | gnd |
| VDD | 5v |
| V0 | 2k resistor to gnd |
| RS | 26 |
| RW | gnd |
| E | 19 |
| D4 | 13 |
| D5 | 6 |
| D6 | 5 |
| D7 | 11 |
| A | 5v |
| K | gnd |

<hr/>

Thank you Matt from raspberrypi-spy.co.uk for supplying the python file for GPIO LCD interaction. That script can be found [here](https://www.raspberrypi-spy.co.uk/2012/07/16x2-lcd-module-control-using-python/).

This has only been tested with Python 2.7, it may or may not work with later versions.

