# LCD-Countdown

This is a library to display a countdown to a certain eepoch time on a 16x2 LCD display using a Raspberry Pi. 

## How to use

To use this script set the epoch time you want to countdown to as the variable `epoch`. 
Also you can change the countdown time with the method `setEpoch(time)`.
You can generate the epoch time at [Epoch Converter](https://www.epochconverter.com/).

**Note**: If the epoch time you set is less than the current epoch time an error will be thrown.

Next, set the text you want to display as a string at variable `text`. You can also set the text by using `setText(message)`.

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

