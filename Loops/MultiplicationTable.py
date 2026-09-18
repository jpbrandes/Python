def multiplication_table():

    numberNfortheTable = input("Type the number you want to see the multiplication table: ")

    for loopprogress_N in range(1,11):
        print("===========================")
        for loopprogress_multiplicand in range(0,11):
            print(f"{loopprogress_N} * {loopprogress_multiplicand} = {loopprogress_multiplicand * loopprogress_N}")
     

multiplication_table()