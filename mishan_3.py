import re
import collections
import random

print("Lab 2 Python")
print("Mishan Regmi 5BCA A '1841030'")

# 1.Explore any 5 string functions in python.
print("\nQuestion 1")
name = input("Enter your name: ")
sur = input("Enter your surname: ")

cap = name.capitalize() #Capitalize the first letter
print("\nAfter capitilization: ", cap)
name = name.capitalize()
sur = name.capitalize()

check = name.endswith('an') #Check the last letter
print("\nChecking the end string of name. ", check)
text = "\nThis is the string you can you to check next function."
print(text)
part = input("\nEnter string to search from text.")
found = text.find(part) #gives the index of the sting to be found

print("\nThe string is found at ", found) 

print("\nMy name is {} .And surname is {}".format(name,sur)) #format the input

start = sur.startswith('R') #check if the string start with 
print("\nChecking the surname starting string. " ,start) 

text2 = " "
a = '12345'
joining = text2.join(a)
print("\nThe String after join is: ", joining)

print("\nQuestion Number 2")

# 2. Given a paragraph

reading = "Python is an interpreted, high-level, general-purpose programming language. Guido van Rossum is the\nfather of python. In the year 1991 pytthon was officially released. Python's design philosophy\nemphasizes code readability with its notable use of significant whitespace.Python follows\nobject-oriented approach. Python is famous as all purpose programming language."
print(reading)
#1 find the most repeated character in the paragraph and turn it to caps. Break the paragraph into lines.
print("\nThe most repeating character is :", collections.Counter(reading).most_common(1)[0])

#2 After splitting into lines find total number of words, lines and characters in the given input.
lineList = len(reading.split('\n'))
print("\nThe number of lines are: ", lineList)

res = len(reading.split()) 
print("The number of words in string are:", res)

cou = len(reading)
print("The number of character are: ",cou)

#3 split the first line using coma as the delimiter.

#4 Fetch the word “Python or python ” from the number of lines (give the word to be searched as user
#  input) replace the word as 'PyThOn'. use suitable inbuilt functions to perform the tasks.
userIn = input("\nEnter the word to be replaced on string. ")
print(reading.replace(userIn,'PyThOn'))

#5. Find a mechanism to give the count of total number of characters excluding whitespaces.

def remove(string): 
    pattern = re.compile(r'\s+') 
    return re.sub(pattern, '', string) 
      
print("\nWithout Space\n",remove(reading)) 

# C. Write a program in python to mimic any word game.

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))

    roll_again = input("Roll the dices again?")