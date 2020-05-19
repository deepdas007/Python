#***********************************************************************************************************
n = "Rodney Dangerfield"
s = -1  # No respect!
print("Hello " + n + ". Your score is " + str(s))
print()
#***********************************************************************************************************


#***********************************************************************************************************
peoples = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in peoples:
    name = person[0]
    score = person[1]
    print("Hello " + name + ". Your score is " + str(score))
print()
#***********************************************************************************************************


#***********************************************************************************************************
num = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for i in num:
    pname = i[0]
    pscore = i[1]
    print("Hello {}. Your score is {}.".format(pname, pscore))
print()
#***********************************************************************************************************


#***********************************************************************************************************
origPrice = float(input('Enter the original price: Rs.'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = 'Rs.{:.2f} discounted by {}% is Rs.{:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)
print()
#***********************************************************************************************************


#***********************************************************************************************************
mylist = ['Deep Das','Mishan Regmi','Raghav Vasan','Triambak Goyal','Sreejit Kar','Aastha Narang','Devaraj Kali']
reverse_list = mylist[::-1]
print("Original List:", mylist)
print()
print("Reversed List:", reverse_list)
print()
#***********************************************************************************************************