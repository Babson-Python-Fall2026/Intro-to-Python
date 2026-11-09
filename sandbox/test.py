size  = 8
middle = size // 2

# rows go from 0 to 3 
for row in range( middle + 1):
    if row == 0:
        print('#' * size)     # print hash line]
    elif row < middle: 
        leading = row - 1     # leading spaces are row - 1
        space_between = size - 4 - 2 * leading # size - 4 chars - 2 * leading
        row = '#' + ' ' * leading + 'x' + ' ' * space_between  + 'x' + ' ' * leading + '#'
        print(row)
    else:
        
        leading = (size - 3) // 2
        row = '#' + ' ' * leading + 'x' + ' ' * leading + '#'
        print(row)

for row in range( middle - 1, -1, -1):
    if row == 0:
        print('#' * size)
    else: 
        leading = row - 1
        space_between = size - 4 - 2 * leading
        row = '#' + ' ' * leading + 'x' + ' ' * space_between  + 'x' + ' ' * leading + '#'
        print(row)
    