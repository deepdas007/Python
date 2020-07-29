def odd(items):
    return items % 2 != 0

nums = [1,2,3,4,5,6,7,8,9,10,11]
print(list(filter(odd, nums)))
