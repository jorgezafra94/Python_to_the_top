# here we are going to learn about
# comprehensions, zip function and enumerate function

print("********************************* comprehensions ********************************************")
# we can create list comprehensions, set comprehensions and dictionaries comprehensions
print('********************* LIST ******************************')
numbers = [1,2,3,4,5,6]
numbers_2 = [num * 2 for num in numbers]
print(numbers)
print(numbers_2)

print('******* if statement ************')
# we can add conditionals

numbers_odd = [num for num in numbers if num % 2 != 0]
print(numbers)
print(numbers_odd)

print('******* else if statement *************')

kind_number = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(numbers)
print(kind_number)

print('********* nested list comprehensions ***********')
new_kind_number = [
    'even'
    if num_2 % 2 == 0
    else
    'odd'
    for num_2 in [num * 2 for num in numbers]
]

print(numbers_2)
print(new_kind_number)

print('************************************** SET ***************************************')
# the set comprehension works as the same as the list comprehension
numbers = [1,1,2,2,3,4,5,5,5,6]
numbers_2 = {num * 2 for num in numbers}
print(numbers)
print(numbers_2)

print('******* if statement ************')
# we can add conditionals

numbers_odd = {num for num in numbers if num % 2 != 0}
print(numbers)
print(numbers_odd)

print('******* else if statement *************')

kind_number = {'even' if num % 2 == 0 else 'odd' for num in numbers}
print(numbers)
print(kind_number)

print('********* nested list comprehensions ***********')
new_kind_number = {
    'even'
    if num_2 % 2 == 0
    else
    'odd'
    for num_2 in [num * 2 for num in numbers]
}

print(numbers_2)
print(new_kind_number)


print('******************************* DICTIONARIES *******************************')
friends = ['Jorge', 'Juan', 'Felipe', 'Messi']
age = [26, 21, 29, 33]
my_dicty = {
    friends[i]: age[i]
    for i in range(len(friends))
}
print(friends, age)
print(my_dicty)
# we can use statements as before but now with dictionaries

my_dicty2 = {
    friends[i]: age[i]
    for i in range(len(friends))
    if i % 2 != 0
}

print(my_dicty2)

print('************************************************************************************')
print('************************************************************************************')

print('************** zip function *********************')
# this function allow us to join 2 or more iterable elements
# normally this elements are list
# it fills until the shortest list of tuples

a = [1,1,1,1,1,1,1,1,1,1,1]
b = [2,2,2,2,2,2,2,2]
c = [3,3,3]

result = list(zip(a,b,c))
print(a, ' ', b, ' ', c)
print(result)

# we can create a dictionary from the zip itself
a = [1,2,3,4]
b = ['a', 'b', 'c', 'd']
result = dict(zip(b, a))
print(result)


print('************* enumerate function ****************')
for i, friend in enumerate(friends):
    print(i, friend)
print('')
# we can also change the starter number
for i, friend in enumerate(friends, start=3):
    print(i, friend)
print('')
result = list(enumerate(friends))
print(result)

result = dict(enumerate(friends, start=2))
print(result)