def cube_of_numbern_function():
    NumberN = input("Type a number to see all their cubes: ")

    for currentnumber in range(0, int(NumberN)):
        cube = currentnumber * currentnumber * currentnumber
        print(f"{currentnumber} and the cube is {cube}")

cube_of_numbern_function()