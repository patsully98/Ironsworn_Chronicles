from random import randint

def action_roll(*args):
	#action roll compares 2 separate 1d10s (the challenge dice) 
	# to 1d6 (the action die) + modifiers
	chal_1 = randint(1, 10)
	chal_2 = randint(1, 10)
	action = randint(1,6)

	for arg in args:
		action += arg

	print(chal_1, chal_2, action)
	
	#Victory conditions:
	#if the action die plus modifiers is greater than both of the challenge dice,
	#you accomplish what you want and remain in control of the situation.
	#if it's greater than only one, you accomplish something but your opponent 
	#seized the advantage and put you . If both challenge dice are greater 
	# than the action die, you've been thwarted and your opponent dictates  
	# theflow of the contest. 
	if action > max(chal_1, chal_2):
		result = "Strong hit"
		return result
	elif action > min(chal_1, chal_2):
		result = "Weak hit"
		return result
	else:
		result = "Miss"
		return result



# this is a test to see if i can pass a dictionary value 
# from a custom class as a function parameter. The real
# character custom class will have stats and I wanted to
# make sure I can put them in a dict.

# class Char:
# 	def __init__(self,name):
# 		self.name = name
# 		self.stats = {
# 		'wits':3,
# 		'edge':2,
# 		'iron':1
# 		}

# bob = Char('bob')

#rolling loop
a = 'y'
while a == 'y':
	a = input("Roll? (y/n) ")
	if a == 'n':
		break
	roll = action_roll()
	print(roll)