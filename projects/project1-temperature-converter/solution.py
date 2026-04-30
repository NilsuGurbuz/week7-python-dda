# Project 1 – Temperature Converter
# Author: Nilsu
# Date: 30.04.2026
#
# Instructions:
# 1. Read the README.md in this folder first.
# 2. Fill in the missing lines below.
# 3. Test with: 0°C -> 32°F | 100°C -> 212°F | -40°C -> -40°F

# — Your solution goes here ————————————————————————————————————————

celsius = float(input("Enter temperature in Celsius: "))


fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")