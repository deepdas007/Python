#*************************************************************
mySlice = "PYTHON"
myRange = mySlice[1:4]
inf_ending = mySlice[2:]
inf_beginning = mySlice[:4]
print(myRange)
print(type(myRange))
print(inf_ending)
print(inf_beginning)
#To print particular set of lists
print([1,3] + [4,5])
#*************************************************************

#*************************************************************
#LISTS AND SLICE OPERATOR
myList = ["My" , "name" , "Deep" , [ "I" , "am" , 19 , "yrs" , "old"] , "Thank" , "you"]
print(myList[2:4])
print(myList[3:])
print(myList[:5])
#*************************************************************

#*************************************************************
#CONCATENATION AND REPETITION
myPCBrand = ["MSI" , "Dell" , "Alienware" , "Razer" , "ROG" , "Asus" , "Lenovo"]
print(myPCBrand + [5 , 6 , 7 , 8 , 9])
print([1,2] * 4)
#*************************************************************

#*************************************************************
#SPLITTING AND JOINING
x = "Hey there Deep here"
s = x.split()
print(s)
s1 = x.split("e")
print(s1)
#*************************************************************

#*************************************************************
myList1 = ["Red","Blue","Green"]
x = ";"
show = x.join(myList1)
print(show)
#*************************************************************

#*************************************************************
#TEST
by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

p = (by,az)
print(p)
x = " ".join(p)
print(x)
q = (x,io)
y = "".join(q)
print(y)
r = (y,qy)
message = ", ".join(r)
print(message)

print(by + " " + az + "" + io + ", " + qy)

message = "".join([by," ",az,"",io,", ",qy])
print(message)
#TEST END

#TRYING
m=[1 , 2 , 3 , 4 , 5]
print(type(m))