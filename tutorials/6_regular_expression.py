import re  # 're' module provides regex support

str = 'an example word:cat!!'
match = re.search('word:[\w]{3}', str)      # searches the string from START to END, for specified pattern

# match return the complete variable,
# match.group() returns the exact text
if match:
    print('Match found "%s"' % (match.group()))
else:
    print('Match not found!!')

match = re.search(r'word:[\w]{3}', str)      # 'r' before the pattern provides raw string, ignores the backslashes

# a, X, 9, < -- ordinary characters just match themselves exactly.
# The meta-characters which do not match themselves because they have special meanings are:
# . ^ $ * + ? { [ ] \ | ( ) (details below)
#
# . (a period) -- matches any single character except newline '\n'
# \w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_].
# Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word.
# \W (upper case W) matches any non-word character.
# \b -- boundary between word and non-word
# \s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ \n\r\t\f]
# . \S (upper case S) matches any non-whitespace character.
# \t, \n, \r -- tab, newline, return
# \d -- decimal digit [0-9] (some older regex utilities do not support but \d,
# but they all support \w and \s)
# ^ = start, $ = end -- match the start or end of the string
# \ -- inhibit the "specialness" of a character. So, for example, use \. to match a period
# or \\ to match a slash. If you are unsure if a character has special meaning, such as '@',
# you can put a slash in front of it, \@, to make sure it is treated just as a character.

# Repetitions are specified by
# '+' -- 1 or more occurences
# '*' -- 0 or more occurences
# '?' -- 0 or 1 occurences

match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')  # found, match.group() == "1 2   3"
match = re.search(r'^b\w+', 'foobar')  # not found, match == None
match = re.search(r'b\w+', 'foobar')  # found, match.group() == "bar"

# [] brackets indicate a set of characters/meta-characters
# Can also indicate a range, so [a-z] matches all lowercase letters.
# To use a dash without indicating a range, put the dash last, e.g. [abc-].
# An up-hat (^) at the start of a square-bracket set inverts it, so [^ab] means any char except 'a' or 'b'.

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'[\w-]+@[\w.]+', str)
if match:
    print( match.group())       # mathces "alice-b@google.com"

# Group Extraction
# Allows you to pick out parts of the matching text. Suppose for the emails problem that we want to extract the username and host separately.
# To do this, add parenthesis ( ) around the username and host in the pattern, like this: r'([\w.-]+)@([\w.-]+)'.
# In this case, the parenthesis do not change what the pattern will match, instead they establish logical "groups" inside of the match text.
# On a successful search, match.group(1) is the match text corresponding to the 1st left parenthesis,
# and match.group(2) is the text corresponding to the 2nd left parenthesis.
# The plain match.group() is still the whole match text as usual.

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w-]+)@([\w.]+)', str)
if match:
    print( match.group())       # mathces "alice-b@google.com"
    print( match.group(1))       # mathces "alice-b" (group-1)
    print( match.group(2))       # mathces "google.com" (group-2)

## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    print(email)


print('---------------Re from file----------------------')
# we can also pass in the file to the findall() to search for all occurences in the file
f = open('../resources/mail_list.txt', 'r')
emails = re.findall(r'([\w\.-]+)@([\w\.-]+)', f.read()) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    print('user=%s | domain=%s' % (email[0], email[1]))

# The option flag is added as an extra argument to the search() or findall() etc.,
# e.g. re.search(pat, str, re.IGNORECASE).
#
# IGNORECASE -- ignore upper/lowercase differences for matching, so 'a' matches both 'a' and 'A'.
# DOTALL -- allow dot (.) to match newline -- normally it matches anything but newline.
# This can trip you up -- you think .* matches everything,
# but by default it does not go past the end of a line.
# Note that \s (whitespace) includes newlines, so if you want to match a run of whitespace
# that may include a newline, you can just use \s*
# MULTILINE -- Within a string made of many lines, allow ^ and $ to match the start and end of each line.
# Normally ^/$ would just match the start and end of the whole string.
str = 'AAFGNF'
match = re.search(r'aafgnf', str, re.IGNORECASE)
if match:
    print(match.group())

# '.*' is Greedy
str = '<b>foo</b> and <i>so on</i>'
match = re.search(r'<.*>', str)
if match:
    print('Greedy match - "%s"' % match.group())

# Add '?' at the end to make it Non-Greedy, PCRE(Perl Compatible Regex)
str = '<b>foo</b> and <i>so on</i>'
match = re.search(r'<.*?>', str)
if match:
    print('PCRE Non-Greedy match - "%s"' % match.group())

# Use inversion within brackets [^>] to make it Non-Greedy
str = '<b>foo</b> and <i>so on</i>'
match = re.search(r'[^>]*>', str)
if match:
    print('Inversion Non-Greedy match - "%s"' % match.group())

## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))  ## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher


