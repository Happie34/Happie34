#year_of_birth = int(input("when were you born"))
#age = 2024 - (year_of_birth)
#print("You are " + str(age) + "years old")

 #Write a script that input the yob and calculate the age.


#birth_year = int(input("when were you born?  "))
#age = 2024 - birth_year
#print("you are " + str(age) + "years old")
#print(type(age))

#Write a script that input the user"s weight in pounds, convert it to kilograms and print on the terminal.
weight_in_pound = float(input("How much do you weigh? "))
weight_in_kg = weight_in_pound * 0.453592
print("You have " + str(weight_in_kg)  + "kgs")

#indexing
course = ("Data Analytics")
print(course[0])
print(course[-2])
print(course[0:])
print(course[3:6])
print(course[:5])


#when you are preparing for python test.
course = ("Data Analytics")
another = course[:]
print(another)

course = ("Beginner_course")
print(course[1:-1])

#formatted string. used to generate some texts with variables.
#To define formatted string:- 
f_name = 'Happie'
l_name = 'Patrick'
message = f'{f_name} {l_name}'
print(message)

#use len to count the characters / limit the characters.
print(len(message))

#methods.
#eg, string methods.
print(f_name.upper())  #upper method
print(f_name.find("a")) #find method
print(f_name.replace('Happie', 'Happiness')) #replace method.
#to check existsnce of a character
print('Happi' in f_name )  #this is boolean

x = 2.9
print(round(x))


import math
print(math.ceil(2.5))
print(math.floor(2.5))
print(math.floor(2.9))

#is_hot = True
#is_cold = False

#if is_hot:
 #print("drink a lot of water")
 #print('enjoy your day')
#elif is_cold:
 #print('is a cold day')

#else:
 #print('wear clothes')
 #print('go away')

#is_hot = True
#if is_hot:
    #print("Drink a lot of water")
    #print("Enjoy your day!")

#if staements

#write a script to tell a user; if its hot tell should drink alot of water, 
# if its cold, tell them; its a cold day, wear warm colthes., 
# and if its neither hot or cold tell them its a lovely day.



