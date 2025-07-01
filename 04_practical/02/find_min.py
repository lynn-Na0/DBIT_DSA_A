def min_num():
    items = [4, 6, 8, 10, 2, 14, 1, 18, 20]
    if not items:
        return None  

    smallest = items[0]  

    for num in items[1:]:
        if num < smallest:
            smallest = num  

    return smallest
print(f"the minimum value is {min_num()}")