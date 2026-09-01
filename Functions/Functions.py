def wisdom():
	print("You have to know when to hold em")

wisdom() # Function called

def fizz_buzz(x):
	if x % 3 == 0 and x % 5 == 0:
		print(f"{x} is FIZZ BUZZ!")
	elif x % 3 == 0:
		print(f"{x} is FIZZ")
	elif x % 5 == 0:
		print(f"{x} is BUZZ")
	else:
		print(f"{x} is Boring")

fizz_buzz(30)

def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False

print(is_even(99))

print("==============")

my_assist_variable = is_even(99)
print(my_assist_variable)