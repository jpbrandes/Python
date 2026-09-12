def product_of_numbers_function():

    first_number = input('Type the first integer number: ') 
    second_number = input('Type the second integer number: ')
    print(f'{first_number} * {second_number} = {int(first_number) * int(second_number)} ')

    if int(first_number) * int(second_number) < 1000:
        print("The product of these two numbers is lower than 1000.")
    elif int(first_number) * int(second_number) > 1000:
        print("The product of these two numbers is greater than 1000.")
    elif int(first_number) * int(second_number) == 1000:
        print("The product of these two numbers is equal 1000.")
    else:
        print("Type again, wrong data entry")

product_of_numbers_function()