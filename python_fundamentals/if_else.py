# if, elif and else statements
# remember be careful with the spaces because that defines if a
# line of code is inside a function, if, or loop

brother = 'Juan'
user_answer = input('what is your name?: ')

if brother == user_answer:
    print('hi my bro')
else:
    print('do i know you?')


# to see if an element is inside a list or tuple or something that can be iterable
# we can use the word 'in'

friends = ['Ivan', 'Felipe', 'Carlos', 'Eddie', 'Kenneth']
others = ['Suarez', 'Messi', 'Kaka']

if user_answer in friends:
    print('aaaa I remember you, Hi friend')
elif user_answer in others:
    print('hi, can we take a picture')
else:
    print('Nop, you are an stranger')