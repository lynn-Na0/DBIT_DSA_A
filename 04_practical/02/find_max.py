def max_num():
    items = [1, 2, 3, 4, 5]
    if not items:
        return None

    max_val = items[0]

    for num in items[1:]:
        if num > max_val:
            max_val = num
    return max_val

print(f"The maximum value is: {max_num()}")
