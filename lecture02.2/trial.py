user_name = input('Please enter your name: ')
user_age = int(input ('Please enter your age: '))
## Age calculator formula
years_to_one_hundred = 100 - user_age
msg = user_name + " you will be 100 in " + str(years_to_one_hundred ) + ' years!'
## print years to 100
## str changes numerical into text
## add spaces ater "" so they don't get stcuk together
print(msg)