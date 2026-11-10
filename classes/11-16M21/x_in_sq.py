''' 
 0123456
0#######     top and bottom all #'s
1#X...X#     lines with 2 x's
2#.X.X.#
3#..X..#     lines with 1 x
4#.X.X.# 
5#X...X#     7 lines, all 7 characters long
6#######


what else do we know?
1) leading spaces = trailing spaces
2) bottom half mirrors the top half
3) if size is the square dimension middle = size // 2
4) won't have lines with 1 x if size is even - simplify assume odd only

Insight: If we print the top half and save each line in a list
we can print the bottom half from that list

wdwk continue:

5) top half loop would have to go from 0 to middle + 1
6) bottom half loop would have to go from middle - 1 to 0
7) 3 types of lines imply 3 conditions
    a) 0 and size - 1 row's get #'s
    b) middle row get's 1 X  leading spaces = trailing spaces = middle - 1
    c) how can we represent all  2 X lines the same way

       i) examine lines 1 and 2
      ii) number of spaces before the first x and after the last x are the same
     iii) leading and trailing spaces are 0 on line 1
      iv) spaces between = size - 4 - 2 * (leading spaces) 

8) for the top half line 0 is #'s, leading spaces for line 1 - 3 = row - 1

'''

size = 7
middle = size // 2
top = []

for idx in range(0, middle + 1):
    ld = idx - 1
    sb = size - 4 - 2 * ld
    if idx == 0:
        row = '#' * size
    elif idx < middle:        
        row = '#' + ' ' * ld + 'X' + ' ' * sb + 'X' + ' ' * ld + '#'
    else:        
        row = '#' + ' ' * ld + 'X' + ' ' * ld + '#'

    print(row)
    top.append(row)

for idx in range(middle - 1, -1, -1):
    print(top[idx])

# another solution comes from the above investigation
# all the type of lines we need are written in the top
# we can use the same code to produce the bottom half 
# if we can create the right index

size = 7
middle = size // 2

#top half
for idx in range(0, middle + 1):
    ld = idx - 1
    sb = size - 4 - 2 * ld
    if idx == 0:
        row = '#' * size
    elif idx < middle:        
        row = '#' + ' ' * ld + 'X' + ' ' * sb + 'X' + ' ' * ld + '#'
    else:        
        row = '#' + ' ' * ld + 'X' + ' ' * ld + '#'
    print(row)

#bottom half
for idx in range(middle - 1, -1, -1): # notice this is the only line that changes
    ld = idx - 1
    sb = size - 4 - 2 * ld
    if idx == 0:
        row = '#' * size
    elif idx < middle:        
        row = '#' + ' ' * ld + 'X' + ' ' * sb + 'X' + ' ' * ld + '#'
    else:        
        row = '#' + ' ' * ld + 'X' + ' ' * ld + '#'
    print(row)

# the top half prints rows 0, 1, 2 and 3
# the bottom half prints out rows 2, 1, 0
'''

rows that are the same
0 = 6
1 = 5
2 = 4
3 = 3
'''

# the above solutions depended on the insight that leading spaces in 
# the top half is equal to row - 1.

# we also notice that the problem is symetrical around the middle
# Is there a way to do this in one loop? To do that we need a formula
# that will compute leading spaces on the basis of the row number.

# consider: leading spaces = middle - abs(middle - row) - 1
# if middle is greater than row what does that reduce to?

# leading spaces = middle - middle + row - 1 = row - 1

'''
size = 7
0  special case #'s
1  ls = 0
2       1 
3  special case 1 x     
4       1
5       0
6   special case #'s

'''

size = 7
middle = size // 2

for idx in range(0, size):
    ld = middle - abs(middle - idx) - 1
    sb = size - 4 - 2 * ld
    if idx in [0, size - 1]:
        row = '#' * size
    elif idx != middle:        
        row = '#' + ' ' * ld + 'X' + ' ' * sb + 'X' + ' ' * ld + '#'
    else:        
        row = '#' + ' ' * ld + 'X' + ' ' * ld + '#'
    print(row)

# Believe it or not, there's actually a 4th way to solve this problem!
# to do so we need to investigate our picture closer:
'''
 0123456
0#######     top and bottom all #'s
1#X...X#     lines with 2 x's
2#.X.X.#
3#..X..#     lines with 1 x
4#.X.X.# 
5#X...X#     7 lines, all 7 characters long
6#######


lets call the line going from top left to bottom right the left diagnol
and the line going from the top right to the bottom left the right diagnol

lets write down the coordinates of each X

left diagnol:  (1,1) (2,2) (3,3) (4,4) (5,5)
right diagnol: (5,1) (4,2) (3,3) (2,4) (1,5)

if we write out each row, 1 column at a time we can use
the above information to create our picture. X's are placed
when row == col or when row + col == size - 1

'''

size = 7
for row in range(size):
    line = ''
    if row in [0, size - 1]:
        print('#' * size)
        continue    
    for col in range(size):
        if col in [0, size - 1]:
            line += '#'
        elif row == col or (row + col) == (size - 1):
            line += 'X'
        else:
            line += ' '

    print(line)


sales = [("Ana", 4000), ("Ben", 9000), ("Ana", 7000),
         ("Cy", 2500), ("Ben", 1000), ("Ana", 4000)]

total_sales = []

print('Ana' in sales[0])
