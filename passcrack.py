import random
numbers = '1234567890abcdefghijklmnopqrstivwxyz'
chars = 'abc123AB,C.!'
guess = ''
pin = ''
guess = input('Enter a length of 4')
while pin != guess:
	pin = random.choices(numbers,k=4)
	pin = ''.join(pin)
	print (f'cracking in progress:{pin}')
print ('your pin is:',pin)
