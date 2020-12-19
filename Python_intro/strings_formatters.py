# string formatting
# here we are going to explain the different ways to convert a variable to string

age = 34
age_as_str = str(age)
result = 'you are ' + age_as_str
print(result)


# we can use f only is we are in python 3.6 or above
result = f'you are {age}'
print('this is with f: ', result)


# also we can use format
result = 'you are {}'.format(age)
print('this is with format: ', result)

# this is another approach about format
# super important
result = 'you are {age}'
final = result.format(age=56)

print(final)