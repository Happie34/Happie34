#Create a program that asks the user for a number and 
#then prints out a list of all the divisors of that number. 

number = input("Enter the number ")
my_number = (1,70,7,10,20,30,40)
for divisor in my_number:
    if divisor % int(number) == 0:
        print(str(divisor) + " is a divisor of " + str(number))
    else:
        print("This is not")



number = input("Enter the number btn 1 and 100 ")
my_number = (1,70,7,10,20,30,40)
for item in my_number:
    divisor = item % int(number)
    if item % int(number) == 0:
        print(str(divisor) + " is a divisor of " + str(number))
    else:
        print("This is not")


#number = input("Enter the number btn 1 and 20 ")
#my_range = range(0,101)
#divisor = my_range[0]
#for item in my_range:
    #if int(divisor) % int(number) == 0:
        #print(str(divisor) + " is a divisor of" + str(number))
    #else:
        #print("This is not it")





