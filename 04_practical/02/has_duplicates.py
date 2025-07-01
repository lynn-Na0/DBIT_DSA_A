def has_duplicates():
    items = [3, 7, 2, 5, 7, 9]

    count = 0
    for item in items:
        count = count + 1
    i = 0
    while i < count:
        j = i + 1
        while j < count:
            if items[i] == items[j]:
                return True
            j = j + 1
        i = i + 1
    return False
print(has_duplicates())
