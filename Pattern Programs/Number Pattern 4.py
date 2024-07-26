'''
123456
12345
1234
123
12
1
12
123
1234
12345
123456

'''

a=int(input('Enter the number of rows : '))
num=1
s=a
for i in range(a+1):
    for j in range(1,a+1):
        print(j,end='')
    a=a-1
    if a>=0:
        print()
for i in range(2,s+1):
    for j in range(1,i+1):
        print(j,end='')
    print()