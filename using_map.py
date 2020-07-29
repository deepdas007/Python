my_list = [1, 2, 3, 4, 5, 6, 7, 8]


def multiply(item):  # A funtion to multiply the given integer values inside the list by 2
    new_list = []  # Creation of new List to store the multiplied value in order to display the expected output
    for i in item:  # Iterating through the list provided outside definition when we use the function with arguments
        # Appending all the multiplied values to the new empty list
        new_list.append(i*2)
    return new_list  # returing the new_list in order to return the output


print()
print('Without using map function:', multiply(my_list))
print()


def new_multiply(data):
    return data*2


# Returns the location of the memory where the included function is stored
print('Location:', map(new_multiply, my_list))
print('Using map function:', list(map(new_multiply, my_list)))
# map function returns the output by taking the action that is needed to be perfrmed inside
# the given function and takes the next argument as the iterables or values for the function that needs to be performed
print()
