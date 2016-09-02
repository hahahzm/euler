import sys

mod = 1000000007

width = int(raw_input("Enter width: "))
height = int(raw_input("Enter height: "))
height = height
choices = height

for x in range(0,width):
	choices = choices % mod
	choices = choices * height

choices = choices % mod
print choices

