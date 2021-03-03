a = [300, 6, 3, 41, 17, 5]

print(sorted(a))  # return a sorted list, !!original list remains unchanged!!
print(sorted(a, reverse=True))   # this is how we sort in reverse order

strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len))  ## custom sorting by passing key function results ['d', 'bb', 'ccc', 'aaaa']
print(sorted(strs))  ## natural order sorting ['aaaa', 'bb', 'ccc', 'd']

strs = ['xd', 'zc', 'yb' ,'wa']

def last_char(str):
    return str[-1]

print(sorted(strs, key=last_char))


# Tuples are like lists, except they are immutable and do not change size
names = {'first': 'John'}
tuple = (1, 2, strs, names)
print(tuple)

# (tuples are not strictly immutable since one of the contained elements could be mutable)
strs = [3, 6]
names['last'] = 'Doe'
# tuple[2] = strs     this will throw an exception

print(strs)
print(tuple)

# A list comprehension is a compact way to write an expression that expands to a whole list
# Syntax: [ expr for var in list ]
numbers = [1, 2, 3, 4, 5]
squares = [n*n for n in numbers]
print(squares)

strs = ['hello', 'and', 'goodbye']

shouting = [s.upper() + '!!!' for s in strs]
print(shouting)  # ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']

# we can also add an condition to the list comprehension syntax as below
squares = [n*n for n in numbers if n%2 == 0]        # this only squares the even numbers into the list
print(squares)

