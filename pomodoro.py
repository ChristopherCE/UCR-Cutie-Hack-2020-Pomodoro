'''
UCR Cutie Hackathon 2020

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
btn1 = io.DigitalInOut(board.D4)
btn1.direction = io.Direction.INPUT

btn2 = io.DigitalInOut(board.D3)
btn2.direction = io.Direction.INPUT

btn3 = io.DigitalInOut(board.D2)
btn3.direction = io.Direction.INPUT

btn4 = io.DigitalInOut(board.D15)
btn4.direction = io.Direction.INPUT

# test LED
led = io.DigitalInOut(board.D14)
led.direction = io.Direction.OUTPUT

# LCD class
lcd = charlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                 lcd_d7, lcd_columns, lcd_rows)

# clear LCD screen
lcd.clear()

while True:
	if(btn4.value == False):
		lcd.clear()
		lcd.message = "BUTTON ON"
		print("BUTTON ON")
		led.value = True
		time.sleep(0.2)
	else:
		lcd.clear()
		lcd.message = "BUTTON OFF"
		print("BUTTON OFF")
		led.value = False
		time.sleep(0.2)
