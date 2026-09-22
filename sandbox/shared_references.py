a = '12'
b = a * 3

print(b)
for l in b:
    print (id(l))  # all '1's and '2's have same id
print()


c = [1,2]
d = c * 3
print(c,d)
print(id(c),id(d)) # c and d different objects, d is one big list
print()

e = [c] * 3  
print(e)      # e is a list of lists
for item in e:
    print(id(item))  #!!! notice that each inner list has the same id.

print()
e[0].append(99)
print(e)

# how can we create a list of lists so each inner list is a different object with unique id
