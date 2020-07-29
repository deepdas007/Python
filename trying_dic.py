my_dict = {
    "Name": ["Deep Das", "Raghav Vasan", "Mishan Regmi"],
    "Age": [19, 20, 23],
    "College": "Christ (Deemed to be University)"

}
# To print the entire dictionary
print(my_dict, "\n")

# To print the value of the given key
print(my_dict["Age"], '\n')

# To access a specific value of list in the dictionary
print(my_dict['Age'][1], '\n')

# To check if the given data is present in the keys or not
print('Friends' in my_dict.keys(), '\n')

# To check if the given data is present in values or not
print('Friends' in my_dict.values(), '\n')

my_dict2 = my_dict.copy()  # To create a copy of the original Dictionary

my_dict2.update({'Age': [30]})  # To update the dictionary
print('Updated Dictionary:', my_dict2, '\n', 'Original Dictionary:', my_dict)

mydict2_pop = my_dict2.pop('Age')  # Deleting a key
print('\nPopped Item:', mydict2_pop, '\n')
print(my_dict2, '\n')


def print_keys():
    for items in my_dict.keys():  # NOTE: If we do not provide the method after the iterable then it would by default print the keys of the dictionary
        print(items)


print_keys()
print()


def print_values():
    for items2 in my_dict.values():  # To display only the values in the dictionary and not the keys
        print(items2)


print_values()
