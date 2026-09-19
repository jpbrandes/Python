def list_checker():
    list_of_numbers = [12, 75, 150, 180, 145, 525, 50, 452, 789]

    for each_item in list_of_numbers:
        if each_item > 500:
            break
    
        if each_item > 150:
            continue
    
        if each_item % 5 == 0:
            print(each_item)

list_checker()