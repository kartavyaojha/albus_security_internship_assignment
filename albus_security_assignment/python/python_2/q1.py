values = '5,7,8,9,0,9,3'
list = [value.strip() for value in values.split(",")]
tuple = tuple(list)

print('List : ', list)
print('Tuple : ', tuple)