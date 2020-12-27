# while and for loop
print('************************** WHILE LOOP ***************************')
print('******* how a while loop works *************')
count = 0
while(count < 5):
    print(count)
    count += 1

# the while loop will review if the condition is True or false
# but it checks always after run the entire code, this per every iteration
# so for example we get the count bigger than 5 at the middle of the loop
# the loop will stop just when it evaluates the condition
print('******** it finishes only when evaluate **************')
count = 0
while(count < 6):
    print(count)
    aux = count
    count = 999
    # I dont care about this value because it wont be the final value
    # so the loop will not stop because of this
    count = aux
    count += 1

# Nota: esto en español, los loops son muy flexibles y  nos permitiran cambiar la condicion
# esto es algo supremamente importante por ejemplo
print('*******modifying condition ***********')
size = 90
count = 0

while(count < size):
    print(count, size)
    count += 1
    size = size // 5

# sometimes we want to stop the loop before the condition fails or in a specific situation
# so that is when we have to use the 'break word'
count = 0
while(count < 999):
    print(count)
    if count == 12:
        break
    count += 1



print('***************** FOR LOOP ***************************')
# the for loops are the most popular loops in python, they can be used 
# in a different ways

# like the while loop
for i in range(5):
    print(i)

names = ['felipe', 'messi', 'antonella']
for name in names:
    print(name)

# when we run over a dictionary, what we are going to have is the keys
a = {'key1': 'val1', 'key2': 'val2', 'kye3': 'vla3'}
for key in a:
    print(key)

for x in a:
    print(x)

# this is another way to print the keys
for x in a.keys():
    print(x)

# in this way we are going to take the values inside the keys
for x in a.values():
    print(x)

# if we want to get keys and values we can use items
# in this way we are gonna have them as tuples
for x in a.items():
    print(x)

# in this way we are going to have them as independent items not tuples
for key, val in a.items():
    print(key, 'and', val)


# lets play with break in for loops
# range(inicio, final, paso)
for i in range(2, 100, 2):
    if i >= 50:
        break
    else:
        print(i)

print('************* else in for loop NEW trick**********************')
print('****** else working *******')
cars = [1, 1, 1, 1]
for car in cars:
    if car != 1:
        break
    print('car is fine')
else:
    print('there werent breaks or problems')

print('***** else not working *********')
cars = [1, 1, 5, 1]
for car in cars:
    if car != 1:
        break
    print('car is fine')
else:
    print('there werent breaks or problems')

print('**************** LIST Comprehension ********************')
# aqui vamos a decir que almacene todos los numeros del 1 al 9
result = [i for i in range(1, 10)]
print(result)
# si queremos meterle condicionales
# en este caso solo meteremos los pares
result = [i for i in range(1, 10) if i % 2 == 0]
print(result)
# si le queremos meter if and else, ojo no se puede elif
result = [i if i%2 == 0 else 'impar' for i in range(1, 30)]
print(result)