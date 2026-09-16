def remove_chars(phrase, NumberNforIndex):
    print("Type a string you want: ", phrase)

    resultExpected = phrase[NumberNforIndex:]

    return resultExpected

print("Removing characters from a string")
print(remove_chars("Hello World", 4))
print(remove_chars("Hello World", 7))
print(remove_chars("Hello World", 2))