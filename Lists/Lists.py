people_names = ["John", "Peter", "Mary", "Jose"]
print(people_names) # If you specify only the name of the list, the program will display all the names it contains. If you specify an index, it will count from zero up to that index.
print(people_names[2])

random_variable = "Tim"
Other_names = ["Carl", random_variable, "Mary", 41]
print(Other_names[1])

random_names = [] # A empty list, it can be filled later.

another_random_names = ["Edward", "April"]
print(len(another_random_names)) # It shows how many items are in this list.

people_names = ["John", "Peter", "Mary", "Jose"]
people_names.append("Bob") # That command add another item to the list.
print(people_names)

people_names = ["John", "Peter", "Mary", "Jose"]
people_names.insert(0, "Bob") # List starts at zero.

people_names = ["John", "Peter", "Mary", "Jose"]
people_names.extend(["Tim","Bob"]) # This command can extend items on a list.

people_names = ["John", "Peter", "Mary", "Jose"]
people_names.remove("Peter") # Remove items

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
names.pop(0)

print("Multidimensional List")

names = ["John", "Mary", "Beatrice", "Bluto", [1,2,3,4]] # To access the internal list, we have to referenciate the position and the number of the element.
print(names[4][2]) # Will print the fourth list and the second element of the fourt element of the list.