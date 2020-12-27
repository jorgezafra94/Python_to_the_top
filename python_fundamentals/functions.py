# how to create funcitons in python
def name_func(arg1, arg2):
    print(arg1, arg2)

name_func('hola', 'chao')

# we can create functions that returns values
# in that way we can asign the returned value to a variable
def func2(x):
    return (x ** 2) / 2

result = func2(3)
print(result, 3)

# also we can use default values in case the user dont put them
def my_math(x=3, y=5):
    return (x * y) / y

print(my_math())
print(my_math(2))
print(my_math(y=4))
print(my_math(y=2, x=8))
print(my_math(2, y=8))
print(my_math(2, 8))

# nota: si el primer argumento lleva nombre de ahi para adelante tendran que llevar nombre
# si no se generará un error
# print(my_math(x=2, 4)) ERRRRRROOOOOOOORRRRRRR!!!!!!!!!!!!!!!!!!!!!!!


print('******************** LAMBDA FUNCTIONS *********************')
# the lambda functions are used to create shorter functions in few lines
def divide1(x, y):
    return x/y

divide2 = lambda x, y: x/y

print(divide1(10, 5))
print(divide2(10, 5))
# with this we can see that they are the same thing


print('******************* full play with lambdas *************************')
# functions
avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operations = {
    'average': avg,
    'total': total,
    'top': top
}

students = [
    {'name': 'Rolf', 'grades': (67, 90, 95, 100)},
    {'name': 'Bob', 'grades': (56, 78, 80, 90)},
    {'name': 'Jen', 'grades': (98, 90, 95, 99)},
    {'name': 'Anne', 'grades': (100, 100, 95, 100)}
]

for student in students:
    name = student['name']
    grades = student['grades']

    print(f'student: {name}')
    operation = input('Enter "average", "total", or "top": ')
    print(operations[operation](grades))