# LCD-Countdown

This is a library to display a countdown to a certain eepoch time on a 16x2 LCD display using a Raspberry Pi. 

## How to use

At the moment the 'countdown.py' script is the one that actually runs the countdown. If you want to change the time to be counuted down to
the 'orlando' variable is the one you are going to want to change. Replace the integer after orlando with the epoch time of your desired date.
You can generate the epoch time at [Epoch Converter](https://www.epochconverter.com/).

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

Thank you Matt from raspberrypi-spy.co.uk for supplying the python file for GPIO LCD interaction. That script can be found [here](https://www.raspberrypi-spy.co.uk/2012/07/16x2-lcd-module-control-using-python/)

