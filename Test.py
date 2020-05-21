#*****************************************************
my_str = "MICHIGAN"
for ch in my_str:
    print(ch)
print()
print()
#*****************************************************


#*****************************************************
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
for i in several_things:
    print(i)

for j in several_things:
    print(type(j))
print()
print()
#*****************************************************


#*****************************************************
#CANNOT USE len FUNCTION
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# Write your code here.
for i in str_list:
    x = 0
    for j in i:
        x = x + 1
    print("Length of item",i,":",x)
print()
print()
#*****************************************************


#*****************************************************
original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0
for i in original_str:
    num_chars = num_chars + 1
print("Length:",num_chars)
print()
print()
#*****************************************************


#*****************************************************
addition_str = "2+5+10+20"
x = addition_str.split("+")
sum_val = 0
for i in x:
    j = int(i)
    sum_val = sum_val + j
    
print("Sum:",sum_val)
print()
print()
#*****************************************************


#*****************************************************
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
my_list = week_temps_f.split(",")
avg = 0
sum = 0
for i in my_list:
    p = float(i)
    avg = avg + 1
    sum = sum + p
    avg_temp = sum/avg
    
print("Average =",avg_temp)
#*****************************************************


#*****************************************************
orginal_str="hello i am good boy"
list_of_words=orginal_str.split()
num_words_list=[]
for i in list_of_words:
    num_words_list.append(len(i))
print(num_words_list)
#*****************************************************


#*****************************************************
lett = ""
var = "b"
for i in range(7):
    lett = lett + var
print(lett)

#*****************************************************