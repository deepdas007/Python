def say_hello(name,age):
	print(f'Hello {name}, your age is {age}')

n = input('Your name here:')
a = int(input('Your age here:'))
say_hello(n,str(a))

def sum1(n1 , n2):
	total = n1 + n2
	return total

print()
print(sum1(5 , 8))
