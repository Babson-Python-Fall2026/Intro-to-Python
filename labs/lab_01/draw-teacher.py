'''
 012345678
0*********
1**-----**
2*-*---*-*
3*--*-*--*         mid = n//2
4*---*---*         idx 0, n-1 print n * '*'
5*--*-*--*         idx mid print * , (mid-1) * ' ', *, (mid-1) * ' ', *
6*-*---*-*         all others
7**-----**         print *, (mid - abs(mid-idx)-1) * ' ', *,  (n - 4 - 2 * (mid - abs(mid-idx)-1)) * ' ', *,(mid - abs(mid-idx)-1) * ' ', *
8*********
'''

txt = 'Enter a positive odd integer: '
while True:
    try:
        n  = int(input(txt))
        if n % 2 == 1 and n > 0: break
        else: raise ValueError
    except ValueError:
        txt = 'Please, enter a positive odd integer: '

mid = n // 2

for idx in range(n):
    if idx in [0,n-1]:
        print(n * '*')
    elif idx == mid:
        
        print(f"*{(mid-1) * ' '}*{(mid-1) * ' '}*")
    else:
        print(f"*{(mid - abs(mid-idx)-1) * ' '}*{(n - 4 - 2 * (mid - abs(mid-idx)-1)) * ' '}*{(mid - abs(mid-idx)-1) * ' '}*")