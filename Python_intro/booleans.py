# booleans
# they are often used in decisions, they only can be true or false

x = True
print(type(x))

x = False
print(type(x))

# we also can have something like this to get some boolean values

age = 20
old_person = age > 30
print(old_person)


# lets create a little script to compare if a input matches with the result

value = 87
user_number = int(input('input your number: '))

answer = value == user_number

print(f'your answer was: {answer}')


# Here we can use the special keys 'and', 'or' to ask different thing in the same line of code
# when we use and, all the conditions have to be true to return a true, in other way it will return false
age = 50
answer = age <= 90 and age> 35
print(answer)

# when we use or, one of all the conditions has to return a True, if all are flase so it will return a false
age = 40
answer = age > 90 or age == 40
print(answer)

result = 20 == 20 or 20 >= 40
print(result)


# not special key
print('using not')
print(not False) # this is going to be True
print(not True) # this is going to be False

result = not(20 == 20 or 20 >= 40)
print(result)

# change to bool
print(bool(None), bool(0), bool([]))
print(bool('h'), bool(123123), bool([1,2,3]))