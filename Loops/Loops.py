number = 0
while number < 10:
	print(number)
	number += 1 # Is the same thing as number = number + 1. Remember to put : on each special block.

print("=============")

random_number = 0
while random_number < 10:
	random_number += 1
	if random_number == 5:
		break
	print(random_number)

print("=============")

for random_number in range(6):
	print(random_number)

for num in range(1,10001):
	if num % 3 == 0 and num % 5 == 0:
		print(f'{num} FIZZ BUZZ')
	elif num % 3 == 0:
		print(f'{num} FIZZ')
	elif num % 5 == 0:
		print(f'{num} BUZZ')
	else:
		print(num)
