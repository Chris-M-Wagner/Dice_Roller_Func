"""
Creator: Chris Wagner
Created Date: 11/25/2015
Last Updated: 11/25/2015

Summary: 
    Roll_Dice is a dice rolling simulation function which takes a user-defined die sides and
    die quantity and outputs a random integer for each die.
"""
import random

def Roll_Dice(sides, die_num):

	if die_num == "":
		die_num = 1

	try:
		sides = int(sides)
		die_num = int(die_num)
	
		if sides <=0 or die_num <=0:
			print "One or both of your inputs is less than 1."
			raise ValueError

	except ValueError:
		while type(sides)!=int or type(die_num)!=int or sides<=0 or die_num<=0:
			print "\nPlease enter a positive integer"
			try:
				sides = int(raw_input("How many sides is each die? "))
				die_num = int(raw_input("How many dice do you want to roll? "))
			except:
				pass

	roll_result = []
	for die in range(0, die_num):
		roll_result.append(random.randrange(1, sides+1))

	if die_num > 1:
		die_dice = "dice"
	elif die_num == 1:
		die_dice = "die"

	print "The outcome of rolling %r %s with %r sides is: %r" %(die_num, die_dice, sides, roll_result)

x = raw_input("How many sides is each die? ")
y = raw_input("How many dice do you want to roll? ")
Roll_Dice(x,y)


'''
Testing Methodology:
1. python Dice Rolling Simulator.py 3 5     ---> Should roll 5 dice with 3 sides
2. python Dice Rolling Simulator.py 3       ---> Should roll 1 die  with 3 sides
3. python Dice Rolling Simulator.py         ---> Should prompt user for die count and die sides, then roll
4. python Dice Rolling Simulator.py 3 pie   ---> Should prompt user for die count and die sides, then roll
5. python Dice Rolling Simulator.py pie 5   ---> Should prompt user for die count and die sides, then roll
6. python Dice Rolling Simulator.py pie     ---> Should prompt user for die count and die sides, then roll
7. python Dice Rolling Simulator.py -1      ---> Should error, prompt user for die count and die sides, then roll
8. python Dice Rolling Simulator.py 3 -5    ---> Should error, prompt user for die count and die sides, then roll
9. python Dice Rolling Simulator.py (input negative or 0)      ---> Should error, prompt user for die count and die sides, then roll
10. python Dice Rolling Simulator.py 0, then input negative vals 2nd time      ---> Should error, prompt user for die count and die sides, error again, then roll
'''