# Lists has a limited manipulation capacity, dictionaries has more controle over the data. You can put any data you like.

favorite_pizza = {
	"John":"Pepperoni",
	"Tim":"Mushroom",
	"Mary":"Cheese",
	"Beatrice":"Ham and Onion", # It is necessary to use comma.
	"Bluto":"Supreme",
}
print(favorite_pizza["John"])

favorite_pizza["Bob"] = "Tuna" # Bob will be associated on the list with the value Tuna.
favorite_pizza.pop("Tim")

print(favorite_pizza)

print(favorite_pizza.keys())
print(favorite_pizza.values())

for names,pizzas in favorite_pizza.items():
	print(f'Key"{names} Value:{pizzas}')

#When you need to access items by an index number, use a List. For all other purposes, use a Dictionary