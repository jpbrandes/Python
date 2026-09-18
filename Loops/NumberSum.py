def sumNnumber():
    accumulator_variable = 0
    numberN = input("Type your desired number: ")
    sumresult = 0

    for accumulator_variable in range(0, int(numberN) + 1):
        sumresult += accumulator_variable
    print(sumresult)
    
sumNnumber()