def List_Fruits():
    list_of_fruits = ["Banana", "Apple", "Graple", "Strawberry", 'Cherry']
    print(f"Printed list: {list_of_fruits}")

    list_of_fruits.append("Fig")
    print(f"Printed list with Fig added: {list_of_fruits}")

    list_of_fruits.append("Elderberry, Raspberry")
    print(f"Printed list with Elderberry and Raspberry added: {list_of_fruits}")

    list_of_fruits.remove("Banana")
    print(f"Printed list with Banana removed: {list_of_fruits}")

List_Fruits()

