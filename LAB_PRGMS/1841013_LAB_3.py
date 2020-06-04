#A. Explore any 5 string functions in python.
#B. Given a paragraph,
#Python is an interpreted, high-level, general-purpose programming language. Guido van Rossum is the father of python. In the year 1991 pytthon was officially released. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Python follows object-oriented approach. Python is famous as all purpose programming language.

#Perform the following tasks:
#1 find the most repeated character in the paragraph and turn it to caps. Break the paragraph into lines.

# 2After splitting into lines find total number of words, lines and characters in the given input.
#3 split the first line using coma as the delimiter.
#4 Fetch the word “Python or python ” from the number of lines (give the word to be searched as user input) replace the word as 'PyThOn'. use suitable inbuilt functions to perform the tasks.
#5. Find a mechanism to give the count of total number of characters excluding whitespaces.

#C. Write a program in python to mimic any word game.

print("               Name - Deep Das")
print("            Register no - 1841013")
print("          LAB 3 - String Operations")


#A. Explore any 5 string functions in python.
wrds = input('Please enter a string here:')
wrds = str(wrds)

print()
print('''          USING 'upper' AND 'lower' FUNCTION''')
if wrds == wrds.upper():
	print('\nString entered is upper case\n')
	small = wrds.lower()
	print('Lower Case of the entered string is',small)

elif wrds == wrds.lower():
	print('\nString entered is lower case\n')
	large = wrds.upper()
	print('Upper Case of the entered string is',large)

print()
print('''       USING 'is' FUNCTION''')
a='Deep Das'
b='Deep Das'
print('\n',a  is b)

print('\n')
left = "           My name is Deep Das"
right = "My name is Deep Das              "
center = "       My name is Deep Das           "

print('\n')
print('''       USING 'strip' FUNCTIONS\n''')
print('Before using lstrip funtion ',left)
lwrd = left.lstrip()
print('\nAfter using lstrip function ',lwrd)

print('\n\n')

print('Before using rstrip funtion ',right)
rwrd = right.rstrip()
print('\nAfter using rstrip function ',rwrd)

print('\n\n')

print('Before using strip funtion ',center)
cwrd = center.strip()
print('\nAfter using strip function ',cwrd)

print('\n\n')

print('''       USING 'replace' FUNCTION''')
print('\n')
a = "Hello my name is Deep Das"
b = a.replace('e','*')
print('Original String',a)
print()
print('String after replace function',b)
print()
print()


para = "Python is an interpreted, high-level, general-purpose programming language. Guido van Rossum is the father of python. In the year 1991 pytthon was officially released. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Python follows object-oriented approach. Python is famous as all purpose programming language."

#1st:- find the most repeated character in the paragraph and turn it to caps. Break the paragraph into lines.
sp=para.split(". ")
print(sp)

res = {}
print()
for keys in para:
       if keys != ' ':
           res[keys] = res.get(keys, 0) + 1

print ("Frequency of all characters in the given input is : \n\n"+ str(res))
print('\n\n')


#2nd:- After splitting into lines find total number of words, lines and characters in the given input.
print('       Length of Words.')
for i in sp:
   wrds = len(i)
print("Length of Words:",wrds)
print()

print('       Length of Lines.')
print ("Length of Lines:", len(sp))
print()

print('       Length of characters')
print("Length of Characters: ",len(para))
print('\n\n')


#3rd:- Split the first line using coma as the delimiter.
fline = sp[0]
print('FIRST LINE:', fline)

wrds_coma=fline.split(",")
print(wrds_coma)
print('\n\n')


#4th:- Fetch the word “Python or python ” from the number of lines (give the word to be searched as user input) replace the word as 'PyThOn'. use suitable inbuilt functions to perform the tasks.
rpl = input("Enter the string you want to replace:")
rpl = str(rpl)

if rpl == 'Python':
	rpl_Python = para.replace('Python','PyThOn')
	print(rpl_Python)
elif rpl == 'python':
	rpl_python = para.replace('python','PyThOn')
else:
	print('''YOU ARE ONLY ALLOWED TO REPLACE 'Python' and 'python' ''')


#5:- Find a mechanism to give the count of total number of characters excluding whitespaces.
x=0
for n in para:
	if n != ' ':
		x = x+1

print()
print("Length of Words (ONLY): ", x)
