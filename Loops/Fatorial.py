def Fatorial_number():
    NumberN = (input("Type a number N for the fatorial calculation: "))
    fatorialcalc = 1

    for factorial_progression in range(1, int(NumberN) + 1):
        fatorialcalc = fatorialcalc * factorial_progression
    print(f"The result of {NumberN} factorial is: {fatorialcalc}")

Fatorial_number()