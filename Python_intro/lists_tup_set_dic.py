# lists tuples sets dictionaries

print('******************************  LIST *************************************')
print('---------------- slicing ---------------------')
a = [1,2,3,4,5,6,7,8]
print(a)
print(a[:])
print(a[1: 4])
print(a[3:])
print(a[:5])
print(a[-2])
print(a[-5: 5])
print('--------------------ADD----------------------------')
a = [1,2,3,4]
b = ['a', 'b', 'c']

#********* add **************
# we can add elements to a list in 4 different ways
# 1. append, this method will add an element at the end of the list
print(a)
a.append(5)

# 2. insert, this method will add an element in a specified position insert(position, value)
# if the position is bigger than the length of the list, it will automatically add it at the end of the list
print(b)
b.insert(2, 'z')
print(b)
b.insert(99999, 'x')
print(b)

# 3. extend, this method allow us to join lists, be careful with the order
c = [1, 'z']
print(c)
c.extend([9, 8, 7, 'f', 'e'])
print(c)

# 4. using + operator
e = [1,2,3]
print(e)
e = e + [5,6,7]
print(e)

print('------------------REMOVE------------------------------')
# ****** remove elements ******
# we can do this in two ways

# 1. remove, this method will let us to remove an element specifying it
a = [1, 'a', 9, 'b', 199]
print(a)
a.remove('b')
print(a)

# 2. pop, this is the most used method to delete elements because we can use the position to this purpose
# remeber if you dont specify a position by default it will take the last element pop()
a = [1, 'a', 9, 'b', 199]
print(a)
a.pop(3)
print(a)

print('---------------------COPY---------------------------')
# to create a copy we should use copy method
z = a.copy()
print(a)
print(z)
print('---------------------REVERSE---------------------------')
# to reverse a list we should use the reverse method
print(z)
z.reverse()
print(z)
print('---------------------SORT---------------------------')
z = [1, 2, 6, 90, 87, -5, 8]
print(z)
z.sort()
print(z)
print('---------------------INDEX---------------------------')
# the index method will allow us to get the index of an element
# if there are more than one same element in the same list
# it will return the position of the first match
z = [2, 3, 4, 5, 6, 7, 5, 9]
print(z, 'this time we are going to get the index of the 5')
res = z.index(5)
print('this was the result, the position of the first match', res)
print('---------------------CLEAR---------------------------')
# with this method we will going to delete all the elements of a list
# and we will have an empty list after apply the method
z = [1,2,3,4,5,1,1,2,3]
print(z)
z.clear()
print(z)
print('---------------------COUNT---------------------------')
# this method will count how many times an element is on the list
z = [1,2,3,4,5,1,1,2,3]
print(z, 'lets count how many 1, and how many 2 are in the list')
print(z.count(1), 'this is the amount of 1')
print(z.count(2), 'this is the amount of 2')
print('if you wanna know more methods of the list please do dir([1])')


print('******************************  TUPLE *************************************')
# tuples dont have many methods
a = (1,2,3)
print(a)
# we can select the element using the position
print(a[0])
# the only way to add elements to a tuple is using + operator
b = a + (4, 5)
print(b)
# we can use slicing to get part of the tuple
c = b[0::2]
print(c)

print('***************************** SET ***********************************')
# NOTEs: the set are not iterables so that is why we cant play with positions
print('---------- ADD ----------')
# with the add method we can add a new element in the set
a = {2,3,4}
print(a)
a.add(5)
print(a)
print('---------- REMOVE ----------')
# with this method we can remove an specified element, as they are unique
# we are going to erase the correct one
print(a)
a.remove(3)
print(a)
print('------ POP --------')
# with this element we will be able to erase the last element of the set
# the problem here is that we CANT SPECIFY the position to erase
print(a)
a.pop()
print(a)
print('-------- INTERSECTION ---------')
# with the sets we can treat them as conjuntos
# so we can get the intersection using & or method .intersection
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
print(a, b)
print('using & for intersection', a & b)
print('--------- UNION -----------')
# using | operator to create the union of sets or .union
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
print(a, b)
print('using | for union', a | b)
print('----------- DIFFERENCES ----------')
# using - t get difference or .difference
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
print(a, b)
print('using - for differences', a - b)
print('------ SYMMETRIC DIFFERENCE ---------')
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
print(a, b)
print(a.symmetric_difference(b))

print('************************** DICTIONARY *********************************')
a = {'a': 23, 4: 'felipe'}
print(a)
print(a['a'], a[4])
print('******** KEYS ************')
keys = a.keys()
print(keys)
print('***** VALUES **********')
val = a.values()
print(val)
print('****** ITEMS **********')
items = a.items()
print(items)
print('******* update **********')
b = {'a': 19, 'b': 90}
print(a)
print(b)
a.update(b)
# here we are going to see how the dictionary change the value in the key a
# and also we are going to see how a new key 'b' is gonna to be created in a dict
print(a)
# how to create a dictionary from a list of tuples
list_tuple = [('jorge', 26), ('juan', 28), ('ivan', 38)]
my_dicty = dict(list_tuple)
print(list_tuple)
print(my_dicty)