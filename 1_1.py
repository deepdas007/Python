#start
print("hello world")

#Operators and Operands
print(4 ** 2) #Exponential expression (4^2)
print((4 + 2)/2)
print(16 - 2 * 5 // 3 + 1) # // gives you the quotient without the deciaml part

#data-types
print(type(13.2)) 
print(type("Hello world"))
print(type(13))

#using variables by assigning values to it
val = 20 #the value 20 is assigned to the variable "val"
print("The value is " +  str(val + 1)) #you have to use "str(whatever variable you have assigned to the no)" in order to use the value which you have assigned to the variable

#type conversion functions
print(3.14 , int(3.14))
print(type(int(3.14)))
print("3.14" , str("3.14"))
print(3.14 , str(3.14) , type(str(3.14))) #gives you the type string
print(3 , float(3) , type(float(3)))
print(3.99 , int(3.99) , type(int(3.99))) #this will not round of to the closest integer, instead it will remove the numbers which are after the decimal point and gives you the output

#printing out the variables
message = "Hello there my friend how are you"
no = 19
print(message)
print(no)
x=5
x=10
print(x)

#Statements and expressions
print(100+200)
print(len("Hello World"))
print(2 * len("Hello") * len("Deep Das"))

#Getting input
n = input("Please enter your name here:")
print("Hello" , n)
print(type(n))
num1 = input("Enter first number here:")
num1 = int(num)
num2 = input("Enter second no here:")
num2 = int(num2)
print("Total = " , num1 + num2)