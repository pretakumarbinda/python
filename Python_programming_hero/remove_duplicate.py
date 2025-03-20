def remove_duplicate(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique
numbers = [22, 11, 3, 1, 4, 5, 5, 2, 2, 11, 66, 89]
print(remove_duplicate(numbers))