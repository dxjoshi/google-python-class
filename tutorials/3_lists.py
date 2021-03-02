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


for i in range(10):     # range(10) #  0 -9
    print(i, end=", ")
print()

for i in range(2, 6):   # range(2,6) #  2-5
    print(i, end=", ")
print()

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
while i < len(a):           # while loop works similar as in java(*break* and *continue* too work)
    print(a[i], end=", ")
    i = i + 1

list = a
print()
print("----------List methods, not functions(called on a list object)---------------")
print(list)
list.append(100)  #  adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
print(list)
list.insert(8, 101)  #  inserts the element at the given index, shifting elements to the right.
print(list)
list2 = [103, 104]
list.extend(list2)  # adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
print(list)
print(list.index(7)) #  searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
list.remove(6)  #  searches for the first instance of the given element and removes it (throws ValueError if not present)
print(list)
list.sort() #  sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
print(list)
list.reverse()  #  reverses the list in place (does not return it)
print(list)
print(list.pop(5)) #  removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).

print(list[1:-2]) # list can also be sliced, 2nd element to 3rd last element