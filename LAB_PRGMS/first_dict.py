my_first = {
	'name':'Deep Das',
	'friends':['Mishan','Raghav','Triambak','Sreejit','Aastha'],
	'friend_age':[22,20,21,20,19],
	'my_age': 18
}

my_second = my_first.copy()

print('\nOriginal Dictionary:', my_first, '\n')
print(my_first.get('nothing', False))
print('name' in my_first.keys(), '\n')
print('Deep Das' in my_first.values(), '\n')
popped = my_first.pop('my_age')
print(popped, '\n')
print(my_first, '\n')
print('Copied Dictionary:', my_second, '\n')
