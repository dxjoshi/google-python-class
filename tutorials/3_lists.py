colors = ['red', 'blue', 'green']
print(colors[0])  ## red
print(colors[2])  ## green
print(len(colors))  ## 3

b = colors  ##  Does not copy the list but both b and colors point to the same list in memory

c = []  # this is an empty list

c = c + colors # + is overloaded to work for list in python
print(c)

for elements in colors: # "for var in list" is the looping construct provided by python
    print(elements, end=" ")

print()
if 'red' in colors:         # can also directly find element in the list using "value in collection"
    print('red color is present')


