import time
import lcd
import math
import RPi.GPIO as GPIO

epoch = 1560247200 # epoch time of event

text = "Countdown to ORL" # message on the top line

""" Sets the epoch time to countdown to """
def setEpoch(t):
    global epoch
    epoch = t

""" Sets the top line text """
def setText(m):
    global text
    text = m
    if(len(text) > 16):
            text = "Text must be < 16"
            
""" Checking that the text is less than 16 characters """
if(len(text) > 16):
    text = "Text must be < 16"
    
""" Setting up the LCD Display """

LINE_1 = lcd.LCD_LINE_1
LINE_2 = lcd.LCD_LINE_2

def main():
    lcd.lcd_init()
    lcd.lcd_string("###SETTING UP###", LINE_1)
    lcd.lcd_string("###SETTING UP###", LINE_2)
    
    lcd.lcd_string(text, LINE_1)
    
    while(True):
        
        time.sleep(.05); # this is to give the pi a cool down
        
        temp_time = epoch - time.time()
        
        """ Calculating the number of days until the specified time """
        days = int(math.floor((epoch - time.time()) / 86400))
        temp_time -= days * 86400 # updating the temp time
        
        """ Calculating the number of hours until the specified time """
        hours = int(math.floor(temp_time / 3600))
        temp_time -= hours * 3600 # updating temp_time
        
        """ Calculating the number of minutes until the specified time """
        minutes = int(math.floor(temp_time / 60))
        seconds = int(temp_time - minutes * 60)
        
        lcd.lcd_string("  %02d:%02d:%02d:%02d" % (days,hours,minutes,seconds), LINE_2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        lcd.lcd_string("   ERROR KBI", LINE_1)
        GPIO.cleanup() # cleaning up GPIO pins
    
