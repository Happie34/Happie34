is_hot = True
is_cold = False
if is_hot:
     print('drink a lot of water')
     print("Or yo will be dehydrated")

#Add else
elif is_cold:
     print("Its cold today")
     print("Dont't go out")

else:
     print("Its a good day")
     print("Wear something warm")

     #price of a house is 1 dollar M,
     #if the buyer has good credit, they need to put down 10%
     #Otherwise they need to put down 20%
     #print the down payment.


good_credit = True
if good_credit:
     down_payment = 10/100*1000000
     print("The down payment is $" + str(down_payment))
else:
      down_payment = 20/100*1000000
      print("down payment is " "$" + str(  down_payment))



#logical opearators.
#if a customer has high income and good credit then,
 #They are eligible for loan.
 
 #We use AND operators to combine two conditions.

#has_high_income = False
#has_good_credit = True

#if has_high_income and has_good_credit:
    # print("Is eligible for loan")

     #Logical or

#has_high_income = True
#has_good_credit = True

#if has_high_income or has_good_credit:
     #print("Is eligible for loan")

 #Logical NOT

has_high_income = True
has_criminal_record = False

if has_high_income and not has_criminal_record:
     print("Is eligible for loan")

     #comparison operators
     #you wanna compare avariable with avalue

     #write a script to tell a user; if the temperature is greater than 30, its a hot day
     # Otherwise if  its less than 10 its a cold day
     # Otherwise its neither hot nor cold.
     
#temp = 30
#f temp > 30:
          #print(" Its a hot day")
     
#elif temp >10:
         # print("Its a cold day")  
#else:
          #rint("Its either hot nor cold")



name = input("what is your name?? ")
if len(name) < 3:
      print("Name must be atleast three characters long")
elif len(name) > 9:
       print("Name can be a maximum of nine characters.")
else:
       print("Name looks good")

       #***weight converter

#weight = input("Enter your weight")
#print("(L)bs or (K)g")

#while loops.
a = 2
while a <= 6:
      print(a)
      a = a + 1
print("well done")













