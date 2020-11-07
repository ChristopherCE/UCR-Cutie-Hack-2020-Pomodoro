'''
UCR Cutie Hack 2020

Pomodoro Study Timer

Programmer: Christopher Alexman
Date: 11/07/2020
'''

import time
import board
import digitalio as io
import adafruit_character_lcd.character_lcd as charlcd

# size of LCD
lcd_columns = 16
lcd_rows = 2

# LCD control inputs
lcd_rs = io.DigitalInOut(board.D22)
lcd_en = io.DigitalInOut(board.D17)
lcd_d4 = io.DigitalInOut(board.D25)
lcd_d5 = io.DigitalInOut(board.D24)
lcd_d6 = io.DigitalInOut(board.D23)
lcd_d7 = io.DigitalInOut(board.D18)

# input buttons
btn0 = io.DigitalInOut(board.D4)
btn0.direction = io.Direction.INPUT
btn1 = io.DigitalInOut(board.D3)
btn1.direction = io.Direction.INPUT
btn2 = io.DigitalInOut(board.D2)
btn2.direction = io.Direction.INPUT
btn3 = io.DigitalInOut(board.D15)
btn3.direction = io.Direction.INPUT

# LCD class
lcd = charlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                 lcd_d7, lcd_columns, lcd_rows)

# clear LCD screen
lcd.clear()


class Pomodoro:
    def __init__(self):
        # btn_0 = 0
        # btn_1 = 1
        # btn_2 = 2
        # btn_3 = 3
        self.long_study = 1500
        self.short_break = 300
        self.long_break = 900

    def start(self):
        lcd.clear()
        lcd.message = "POMODORO\nButton: 1-4"
        time.sleep(3)

    def study(self):
        while self.long_study:
            mins, secs = divmod(self.long_study, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            lcd.clear()
            lcd.message = timer
            time.sleep(1)
            self.long_study -= 1

    def shortBreak(self):
        while self.short_break:
            mins, secs = divmod(self.short_break, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            lcd.clear()
            lcd.message = timer
            time.sleep(1)
            self.short_break -= 1

    def longBreak(self):
        while self.long_break:
            mins, secs = divmod(self.long_break, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            lcd.clear()
            lcd.message = timer
            time.sleep(1)
            self.long_break -= 1

    def reset(self):
        lcd.clear()
        self.long_study = 1500
        self.short_break = 300
        self.long_break = 900

    def stop(self):
        lcd.clear()


def main():
    p = Pomodoro()
    p.start()


if __name__ == "__main__":
    main()


# test it up
'''
while True:
    if btn0.value is False:
        lcd.clear()
        lcd.message = "BUTTON ON"
        print("BUTTON ON")  # debugging
        time.sleep(0.2)
    else:
        lcd.clear()
        lcd.message = "BUTTON OFF"
        print("BUTTON OFF")  # debugging
        time.sleep(0.2)
'''
