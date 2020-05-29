#DOMAIN - GAMING
#LAB - 1 (Different Games Shopping)

print()
print("         1. PUBG - Rs. 999")
print("         2. GTA 5 - Rs. 2500")
print("         3. Call of Duty:Modern Warfare - Rs. 3999")
print("         4. Rust - Rs. 899")
print("         5. Red Dead Redemption - Rs. 3000")

games = ['PUBG','GTA 5','Call of Duty:Modern Warfare','Rust','Red Dead Redemption']
prices = [999,2500,3999,899,3000]

gnum = input("Enter the total games you want to purchase out of the options:")
gnum = int(gnum)
print()

print("         1. PUBG - Rs. 999")
print("         2. GTA 5 - Rs. 2500")
print("         3. Call of Duty:Modern Warfare - Rs. 3999")
print("         4. Rust - Rs. 899")
print("         5. Red Dead Redemption - Rs. 3000")
print()
print("                    Choose which games do you want to purchase:")
print()

sum1 = 0
sum1 = float(sum1)
total = 0
total = float(total)

for i in range(gnum):
	gnum2 = input()
	gnum2 = int(gnum2)
	if gnum2 == 1:
		sum1 = sum1 + prices[0]
		print("Game Choosen - {}, Price - Rs. {}".format(games[0],str(prices[0])))
		print()

	elif gnum2 == 2:
		sum1= sum1 + prices[1]
		print("Game Choosen - {}, Price - Rs. {}".format(games[1],str(prices[1])))
		print()

	elif gnum2 == 3:
		sum1 = sum1 + prices[2]
		print("Game Choosen - {}, Price - Rs. {}".format(games[2],str(prices[2])))
		print()

	elif gnum2 == 4:
		sum1 = sum1 + prices[3]
		print("Game Choosen - {}, Price - Rs. {}".format(games[3],str(prices[3])))
		print()

	elif gnum2 == 5:
		sum1 = sum1 + prices[4]
		print("Game Choosen - {}, Price - Rs. {}".format(games[4],str(prices[4])))
		print()

print()
total = total + sum1
total1 = total + (total * 0.18)
total1 = float(total1)

print("Your Amount is Rs. {}".format(str(total)))
print()
print("Your Grand Total is (After adding GST amount) Rs. {}".format(str(total1)))