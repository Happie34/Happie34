#01. Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("What is your name? ")
age = input("What is your age? ")
current_year = input("current year ")
year_of_birth = int(current_year) - int(age)
yearin100 = year_of_birth + 100
print("you will be 100 years old in " +str(yearin100) )

#2. Ask the user for a number. Depending on whether the number is even or odd,
#  print out an appropriate message to the user.

number = int(input("Enter a number "))
if number % 2 == 0:
    print("This is an even number ")
else:
    print("This is an odd number ")

    #3.Take a list, say for example this one:
   #[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 #and write a program that prints out all the elements of the list that are less than 5.


list = (2,3,5,7, 12, 16, 20)
for number in list:
    if number < 10:
        print(str(number) + " is less than ten")
else:
    print(str(number) + " is greater than ten")

    

    #4.
    #Create a program that asks the user for a number 
    #and then prints out a list of all the divisors of that number.



#print([i for i in range(1,n+1) if n%i==0])



number = input("Enter the number btn 1 and 100 ")
my_number = (1,70,7,10,20,30,40)
for item in my_number:
    divisor = item % int(number)
    if item % int(number) == 0:
        print(str(divisor) + " is a divisor of " + str(number))
    else:
        print("This is not")


#A program that writes the maximum number.
numbers = (1,2,3,4,5,6,7)
for max in numbers:
    if max > numbers:
        print("This is the maximum number")

























list_of_students = ["Michele", "Sara", "Cassie"]

name = input("Type name to check: ")
if name in list_of_students:
    print("This student is enrolled.")













    

   





