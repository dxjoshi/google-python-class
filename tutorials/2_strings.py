"""
3 double quotes
used for a
multiline
comment
"""

str1 = 'We can use "double quotes" and \'single quote\' in a string literal.'
str2 = "\nAlso can create a string literal by using double quotes."

str2 = str1 + str2  # creates a 3rd string as string are immutable in python
print(str2)

print(str2[0])  # Can fetch character using [] based syntax. Has zero-based indexing

pi = 3.14
# text = 'The value of pi is ' + pi      # NO, does not work
text = 'The value of pi is ' + str(pi)  # yes
print(text)

print(5 / 6)  # for floating point division
print(7 // 6)  # for integer based division

raw = r'this\t\n and that'  # for raw string, passes all characters without backslash treatment

print(raw)

s = 'Python'
print(s.lower(), s.upper())  # returns the lowercase or uppercase version of the string
print(s.strip())  # returns a string with whitespace removed from the start and end
print('%s %s %s ' % (s.isalpha(), s.isdigit(), s.isspace()))  # tests if all the string chars are in the various
# character classes
print(s.startswith('P'), s.endswith('n'))  # tests if the string starts or ends with the given other string
print(s.find('Py'))  # searches for the given other string (not a regular expression) within s, and returns the first
# index where it begins or -1 if not found
print(s.replace('Py', 'PY'))  # returns a string where all occurrences of 'old' have been replaced by 'new'
input_list = ['aaa', 'bbb', 'ccc']
s = ','
s = s.join(input_list)
print(s)
print(s.split(','))  # returns a list of substrings separated by the given delimiter. The delimiter is not a regular
# expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case
# s.split() (with no arguments) splits on all whitespace chars.

print('------------slice function 0-based index------------')
s = 'Hello'

print(s[1:3], s[1:100])     # end index excluded or reduced to string length when necessary
print(s[1:])    #
print(s[:3])
print(s[:])
print(s[:1] + s[1:])    # return the original string

print('------------slice function negative index------------')
print(s[-1])    # last character
print(s[-3:])   # third last till end of string
print(s[:-3])

print('------------% usage with strings------------')
print('I am %s, son of %s' %('Thor', 'Odin'))  # %d int, %s string, %f/%g floating point

# Split the line into chunks, which are concatenated automatically by Python
text = (
        "%d little pigs come out, "
        "or I'll %s, and I'll %s, "
        "and I'll blow your %s down."
        % (3, 'huff', 'puff', 'house'))

print(text)

print('----------If-Else-----------')
speed = 100
mood = 'bad'
if speed >= 80:
    print('License and registration please')
if mood == 'terrible' or speed >= 100:
    print('You have the right to remain silent.')
elif mood == 'bad' or speed >= 90:
    print("I'm going to have to write you a ticket.")
else:
    print("Let's try to keep it under 80 ok?")

