import random
try:
	number = int(input(''))
	guess = 0
	Trial = 0
	while guess != number:
		guess = (random.randint(0000,9999))
		Trial += 1
		print ('Trial' + '___' + str(Trial) + ' . . . .' + str(guess) + ' Hacking in Progress . . . . . . . . . . ')
	print (f'_Hacked___ . . . . .Your Password is:' + str({guess}) + '. . . . . . . . . . . ')
except ValueError:
	print ('number only, its a pin hacker dude')
