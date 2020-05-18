#*************************************************************
num = range(10)
sum = 0
print()
for i in num:
	sum = sum + i
	print("i = ", i,"," , "Sum = " , sum)
print()
print("Total = ",sum)
#*************************************************************

#*************************************************************
print()
print()
num = range(10)
print("Type: ",type(num))
#*************************************************************

#*************************************************************
print()
print()
original_str = "The quick brown rhino jumped over the extremely lazy fox"
x = original_str.split(" ")
for i in x:
    num_words_list = len(i)
    print(num_words_list)
    
#*************************************************************