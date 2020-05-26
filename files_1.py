#*********************************************************************************************
var = open('emotion_words.txt','r')
lines = var.readlines()
num_lines = 0
for i in lines:
    num_lines = num_lines + 1
print(num_lines)
var.close()
print()
#*********************************************************************************************


#*********************************************************************************************
olypmicsfile = open("olypmics.txt", "r")

for aline in olypmicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()
print()
#*********************************************************************************************