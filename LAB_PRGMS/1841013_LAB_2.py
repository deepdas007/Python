print('\n         Name - Deep Das')
print('      Register No - 1841013')
print('      Program 2 - Calculator\n')

import math

print(" 1. Simple Calculator\n 2. Scientific Calculator\n 3. Company Program\n Type 'done' if you are done")

d = 0

while d < 1:
  ch = input("\nChoose your calculation. ")
  if ch != 'done':
    if ch == '1':
      print("Simple Calculator\n") 
      print("Please select operation:\n")
      print(" 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n \nEnter 'done' if you are done.") 
      i = 0

      while i < 1:
        choice = int(input("\nSelect operations:"))
       
        if choice != 'done':  
          num1 = float(input("\nEnter first number: ")) 
          num2 = float(input("Enter second number: ")) 
        
          if choice == 1: 
            print("Result:", num1, "+", num2, "=", str(num1 + num2)) 
        
          elif choice == 2: 
            print("Result:", num1, "-", num2, "=", str(num1 - num2)) 
        
          elif choice == 3: 
            print("Result:", num1, "*", num2, "=",  str(num1 * num2)) 
        
          elif choice == 4: 
            print("Result:", num1, "/", num2, "=", str(num1 / num2)) 
         
          else: 
            print("Invalid input. Please enter again.") 
       
        else:
          i = i + 1
          break
    
    elif ch == '2':
      print ("\nScientific Calculator")
      print('''
      Operator Available
      ^     for power
      r     for root
      %     for modulus
      pie   for Pie
      sin   for sin (trig)
      cos   for cos (trig)
      tan   for tan (trig)
      !     for factorial 
      ln    for ln (log function)
      ''')
      opt = input("Enter the operator: ").lower()
      fnum = float(input("Enter first number: "))
      snum = float(input("Enter second number: "))

      if opt == "^":
          print (fnum, "^", snum, "=", fnum ** snum)
      
      elif opt == "r":
          print (fnum, "root", snum, "=", snum ** (1 / fnum) )
      
      elif opt == "%":
          print (fnum, "%", snum, "=", fnum % snum )
      #factorial
     
      elif opt == "!":
          theNumber = fnum = snum 
          snum = 1
          
          while fnum > 1:
              snum *= fnum 
              fnum = fnum - 1  
          print ("n!(", theNumber, ")=", snum )
     
      elif op == "sin":
          print ("sin(", snum, ")=", math.sin(snum ))
      
      elif op == "cos":
          print ("cos(", snum, ")=", math.cos
          (secondNumber ))
      
      elif op == "tan":
          print ("tan(", snum, ")=", math.tan(snum ))
     
      elif op == "pie" or op == "pi":
          print ("Pie =", math.pi)
      
      elif op == "ln":
          print ("ln(", snum , ")= ", math.log(snum))
     
      else:
          print ("incorrect operator") 
      
    elif ch == '3':
      
      print("\nBank Application\n")
      rev = float(input("Enter company's year revenue."))
      sales = float(input("Enter the sales of the year."))
      exp = float(input("Enter the total expenses of the year."))
      i = 0

      while i < 1:
        print("\n 1. Calculate yearly profit and Quaterly\n 2. Check Growth \nType 'done' if your work is finished")
        che = int(input("\nChoose what you want to do."))
        
        if che != 'done':
          
          if che == 1:
            profit = rev - exp
            print("\nYour profit of this year is", profit)
            firstQ = profit/4
            print("\nYour company made a profit of Rs.", firstQ ,"in the first quarter.")
          
          elif che == 2:
            
            if (profit < exp):
              print("\nCompany is growing keep working hard.")
           
            else:
              print("\nNeed more inprovemnt in finance management.")
          
          else:
            print("Invalid choice.")
            pass
       
        else:
          i = i + 1
          break
      
      else:
        print("Invalid Input")
  
  else:
    d = d + 1
    print("\nThank You")
    break