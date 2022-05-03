"""
PROGRAM JamEx Commision Rate:
Author: Lavon Francis
Date: April 29, 2022
Course: ITT103
Purpoae: This program was designed to calculate the comission earned
by sales persons employed to JamEx Limited.
"""

ans = '1'
while ans != '2' : #Loops the program until the user enters the end key "2"
  
#This will repeat the request for the user to input a figure until a valid figure has been entered.
  while True: 
    try:
      sales_amount = float(input("Please enter Sales Amount $"))
      if sales_amount > 0:
        break
      print('"Invalid Sales Amount"')
    except Exception as sa:
      print('"Sales Amount Must be A Number"')
      
    while True: 
    try:
      salesperson_number = int(input("Please enter Salesperson Number "))
      if sales_amount > 0:
        break
      print('"Invalid Salesperson Number"')
    except Exception as sa:
      print('"Input Must be A Number"')   
  
#This will repeat the request for the user to input a class number until a
#valid number is entered. Only 1, 2 or 3 will be accepted as valid.
  while True:
      try:
        class_number = int(input("Please select Salesperson Class 1,2 or 3 "))
        if class_number > 0 and class_number < 4:
          break
        else:
          print('"Input Must be a number between 1 and 3"')
      except Exception as cn:
        print('"Input Must be a number between 1 and 3"')

  sales_amount = float(sales_amount)
  class_number = str(class_number)
  if class_number == '1': 
    if sales_amount > 0 and sales_amount < 1001:
      com_rate = 0.06
    elif sales_amount > 1000 and sales_amount < 2000:
      com_rate = 0.07
    elif sales_amount == 2000 or sales_amount > 2000:
      com_rate = 0.10
    else:
      com_rate = 0
  elif class_number == '2':
    if sales_amount > 0 and sales_amount < 1000:
      com_rate = 0.04
    elif sales_amount == 1000 or sales_amount > 1000:
      com_rate = 0.06
    else:
      com_rate = 0
  elif class_number == '3':
    if sales_amount > 0:
      com_rate = 0.045
    else:
      com_rate = 0 
  else:
    print("Involid Class")
    com_rate = 0
  com = sales_amount * com_rate
  print("Sales Person ID", salesperson_number)
  print("Commission is $",com)
  print("Commission Rate is ", com_rate)
  ans = input("Press ANY Key to Continue or 2 to END ")
