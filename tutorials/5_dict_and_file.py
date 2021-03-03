dict = {}  #  empty dictionary

dict[0] = 'zero'
dict[1] = 'one'

print(dict, dict[1])

if 'x' in dict:
    print(dict['x'])

# print(dict['y'])    # throws key error
print(dict.get('y'))        # prints none if the key is not present
print(dict.get('y', 'Key not present'))        # prints second argument value, if the key is not present

dict = {'a': 'alpha', 'g': 'gamma', 'o': 'omega'}
## By default, iterating over a dict iterates over its keys.
## Note that the keys are in a random order.
for key in dict: print(key, end=" ")     ## prints a g o
print()
## Exactly the same as above
for key in dict.keys(): print(key, end=" ") ## Get the .keys() list:
print()

print(dict.keys())  ## ['a', 'o', 'g']

## Likewise, there's a .values() list of values
print(dict.values())  ## ['alpha', 'omega', 'gamma']

## Common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(dict.keys()):
    print(key, dict[key])

## .items() is the dict expressed as (key, value) tuples
print(dict.items())  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

## This loop syntax accesses the whole dict by looping
## over the .items() tuple list, accessing one (key, value)
## pair on each iteration.
for k, v in dict.items(): print(k, '>', v)  ## a > alpha    o > omega     g > gamma

hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s' % hash
# %d for int, %s for string --> 'I want 42 copies of garfield'

var = 6
del var  # var no more!

list = ['a', 'b', 'c', 'd']
del list[0]  ## Delete first element
del list[-2:]  ## Delete last two elements
print(list)  ## ['b']

dict = {'a': 1, 'b': 2, 'c': 3}
del dict['b']  ## Delete 'b' entry
print(dict)  ## {'a':1, 'c':3}

print('----------------File-----------------------')
# python reads file loading one line at a time into the memory
# The f.readlines() method reads the whole file into memory
# and returns its contents as a list of its lines.
# The f.read() method reads the whole file into a single string,
# which can be a handy way to deal with the text all at once,
# such as with regular expressions
# f = open('1_intro.py', 'rU')        #  'r' for read mode 'U' for universal line endings
# for line in f:
#     print(line)
# f.close()

# 'r' - open for reading (default)
# 'w' - open for writing, truncating the file first
# 'x' - create a new file and open it for writing
# 'a' - open for writing, appending to the end of the file if it exists
# 'b' - binary mode
# 't' - text mode (default)
# '+' - open a disk file for updating (reading and writing)
# 'U' - universal newline mode (deprecated)

# f = open('1_intro.py', 'a')        #  'r' for read mode 'U' for universal line endings
# f.write('append')
# f.close()


import codecs

f = codecs.open('1_intro.py', 'rU', 'utf-8')
for line in f:
    print(line)  # here line is a *unicode* string


