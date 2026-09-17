def NumberSwitching():
    
    number_A = input("Type your number: ")
    number_B = input("Type your second number: ")
    print(f"Before Swap: numberA = {number_A}, numberB = {number_B}")

    number_A, number_B = number_B, number_A

    print(f"After Swap: numberA = {number_A}, numberB = {number_B}")

NumberSwitching()