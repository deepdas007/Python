fileref = open("olympics.txt", "r")

contents = fileref.read()
lines = fileref.readlines()

for line in lines[:7]:
    print(line.strip())
print()
for i in fileref:
    print(i)
    
fileref.close()