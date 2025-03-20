
iterable_value = 'Preta Kumar Binda'
iterable_object = iter(iterable_value)

while True:
    try:
        item = next(iterable_object)
        print(item)
    except StopIteration:
        break