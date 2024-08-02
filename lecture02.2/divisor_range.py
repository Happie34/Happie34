

number = input("Enter the number ")
my_range =range(0,101)
for divisor in my_range:
    if divisor % int(number) ==0:
        print(str(divisor) + " is the divisor of " + str(number))
    #else:
       #print("It is not it")

#A program that writes the maximum number.
#numbers = (1,2,3,4,5,6,7)
#max = numbers[0]
#for max in numbers:
    #if max > numbers:
        #print("This is the maximum number")

#use maximum built in function.
numbers = (1,2,3,4,5,6,7)
maxi = max(numbers)
print("The maximum no is " + (str( maxi)))

# Two dimensional lists.(matrix)
#*Each item in the list is another list

#List method.

#numbers = [1,2,3,4,5,6,7]
#numbers.insert (4,10)
#print(numbers)
 #numbers.pop - removed the last numbers.
 #numbers.index - pass the index of a number and
 #check for the existance of an item.

#print(numbers.index(5))
# count the number of a value
#print (numbers.count(5))

#sort- used to sort the list #
# in accesinding or descending.
#numbers.sort()
#print(numbers)
#numbers.reverse - sort in descending// reverse
#numbers2 = numbers.copy()
#print(numbers2)
 
 #Eliminate duplicates.
numbers = [2, 3, 4, 5, 5, 6, 2, 3] 
unique = []
for item in numbers:
    if item not in unique:
        unique.append(item)
print(unique)

#Turples.

#Are similar to list, but cant be modified.
#we use square brackets to define list and parenthesis to define tuples.


