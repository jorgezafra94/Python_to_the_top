# there are two kind of numbers in python integers or floats
# this is a integer
x = 123
print(type(x))

# this is a float numbre
x = 123.988891
print(type(x))

# we can develop some operations
y = 1 + 6 / 3 * 3
print(y)

y = 12.4 / 2.3
print(y)

# to remove the decimal places we can use // operator
# this operator just gave us the integer part

y = 9 / 4
print(y)

y = 9 // 4
print(y)

# now if you want to get the residual of a division
# you can use the % operator

y = 9 % 3
print('here the residual should be 0: ', y)

y = 9 % 2
print('here the residual should be 1: ', y)
# here is 1 because 2 * 4 = 8 ----> 9 - 8 = 1

y = 14 % 5
print('here the residual should be 4: ', y)
# here is 4 because 5 * 2 = 10 ---> 14 -10 = 4