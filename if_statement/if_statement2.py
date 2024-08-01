#for loops.
#used to iterate items of a collection. i.e a string.
#in each iteration the variable holds one character.
#used to iterate each character in astring.
for name in "Happy":
    print(name)
    #2.
name = ("Happy" "patrick" "letty")
for name in ["Happy ", "patrick " ,"letty ",]:
    print(name)
   
    #range function.
for numbers in range(11):
    print(numbers)

for numbers in range(5, 9):
    print(numbers)

   #calculate the total cost of all items in a cart
#cost =  (20, 30, 40)
#total_cost = 0
#for total_cost in cost:
    #total_cost = total_cost + cost
    #print("The " + "cost " + "is " + str(total_cost))


cost = (20, 30, 40)
total_cost = 0
for items_cost in cost:
    total_cost += items_cost
print("The total cost is $" + str(total_cost))
    
    #3nested loops
    #Adding one loop inside of another loop.
    

#challenge
while a <= 6:
      print(a)
      a = a + 1
print("well done")

    


