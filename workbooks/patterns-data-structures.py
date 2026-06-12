

'''


txt = 'input an integer: '
while True:
    try:
        number = int(input(txt))
    except ValueError:
        txt = 'please input an integer: '
    else:
        break


'''

from pprint import pprint as pp
dim_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

rows = 2
cols = 5

dim_2 = []


for i in range(rows):
    row = []
    for j in range(cols):
        
        idx = i * cols + j       
        row.append(dim_1[idx])
    
    dim_2.append(row)

pp(dim_2)
    

dim_1 = []
pp(dim_1)
for idx in range(rows * cols):

    i = idx // cols
    j = idx % cols

    dim_1.append(dim_2[i][j])

pp(dim_1)





fruit = ['grapes', 'oranges', 'apples', 'pears', 'blueberries']

cnt = 0
length = len(fruit)
while cnt < 13:
    print(cnt + 1, fruit[cnt % length])
    cnt += 1
    if cnt % length == 0: print()
    