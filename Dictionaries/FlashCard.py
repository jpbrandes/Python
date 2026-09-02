import random
our_rand = random.randint(1,10)
print(our_rand)

from os import system 

# Addition flashcard function
def add_flashcard():
	system("cls")
	card_one = random.randint(0,10)
	card_two = random.randint(0,10)

	correct = card_one + card_two

	answer = input(f'{card_one} + {card_two}: ')

	if int(answer) == correct:
		print(f'Correct! {card_one} + {card_two} = {answer}')
	else:
		print(f'Wrong! {card_one} + {card_two} = {correct}')
	play = input("Would you like another card? yes|no|restart: ")

	if play.lower() == "yes":
		add_flashcard()
	elif play.lower() == "no":
		print("Thanks for playing!")
	elif play.lower() == "restart":
		start_game()
	else:
		print(f'Sorry, I dont recognize {play}')
		input("Please hit enter to try again.")
		add_flashcard()

# Subtraction flashcard function
def subtract_flashcards():
	system("cls")
	card_one = random.randint(0,10)
	card_two = random.randint(0,10)

	correct = card_one - card_two
	answer = input(f'{card_one} - {card_two}: ')

	if int(answer) == correct:
		print(f"Correct! {card_one} - {card_two} = {answer}")
	else:
		print(f'Wrong! {card_one} - {card_two} = {correct}')

	play = input(f'Would you like another card? (yes|no|restart): ')

	if play.lower() == "yes":
		subtract_flashcards()
	elif play.lower() == "no":
		print("Thanks for playing!")

	elif play.lower() == "restart":
		start_game()
	else:
		print(f'Sorry, i dont recognize {play}')
		input("Please hit enter to try again ")
		subtract_flashcards()


# Multiply flashcard function
def multiply_flashcards():
	system("cls")

	card_one = random.randint(0,10)
	card_two = random.randint(0,10)

	correct = card_one * card_two

	answer = input(f'{card_one} * {card_two}: ')

	if int(answer) == correct:
		print(f"Correct! {card_one} * {card_two} = {answer}")
	else:
		print(f'Wrong! {card_one} * {card_two} = {correct}')

	play = input(f'Would you like another card? yes|no|restart:')

	if play.lower() == "yes":
		multiply_flashcards()
	elif play.lower() == "no":
		print("Thanks for playing!")

	elif play.lower() == "restart":
		start_game()
	else:
		print(f'Sorry, i dont recognize {play}')
		input(f'Please hit enter to try again ')
		multiply_flashcards()

# Division flashcard function

def divide_flashcards():
	system("cls")
	card_one = random.randint(0,10)
	card_two = random.randint(1,10)

	correct = card_one / card_two

	answer = input(f'{card_one} / {card_two}: ')

	if float(answer) == correct:
		print(f'Correct! {card_one} / {card_two} = {answer}')
	else:
		print(f'Wrong! {card_one} / {card_two} = {correct}')

	play = input(f'Would you like another card? yes|no|restart: ')

	if play.lower() == "yes":
		divide_flashcards()
	elif play.lower() == "no":
		print("Thanks for playing!")
	elif play.lower() == "restart":
		start_game()
	else:
		print(f'Sorry. i dont recognize {play}')
		input("please hit enter to try again")
		divide_flashcards()



# Function to start the game and pick cards

def start_game():
	system("cls") # clear screen for clarity
	print("Welcome to Math Flashcard game!")
	pick = input("Choose your flashcard (add|subtract|multiply|divide): ")

	if pick.lower() == "add":
		add_flashcard()
	elif pick.lower() == "subtract":
		subtract_flashcards()
	elif pick.lower() == "multiply":
		multiply_flashcards()
	elif pick.lower() == "divide":
		divide_flashcards()
	else:
		print(f'Sorry, try a correct input.')
		input("Please hit enter to try again ")

	start_game()

start_game()