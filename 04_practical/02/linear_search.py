def search_target():
    items = [10, 23, 25, 45, 72, 88]  
    target = 72                   

    index = 0
    for value in items:
        if value == target:
            return index
        index += 1

    return -1  
print(search_target())  
