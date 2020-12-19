# strings
# the string are just like expressions, words, sentences, paragraphs, etc

my_string = 'hello everybody'
print(my_string)
# to create strings we can use single quotes or doble quotes

my_string = "hello everybody"
print(my_string)

# there is something important to say and it is that
# if we have to use one type of quotes inside the string we have to use the other
# to close the string

my_string = 'he said "bye bye world" yesterday before he went'
print(my_string)

my_string = "that's the Marrie's dog"
print(my_string)

# also there is another type of string that we can create from quotes
# and is using triple doble quotes
# the advantages of this way is that we can handle new lines without
# using the \n command

my_string = """
Hello

Everybody
"""

print(my_string)


my_string = 'Hello\n\nEvrybody'
print(my_string)


# we can also concatenate the strings using the + symbol

first = 'hello '
second = 'world'

result = first + second
print(result)

# remember this only works with variables with the same type