'''
* 
* * 
* * * 
* * * * 
* * * * *
* * * *
* * *
* *
*

'''
a=int(input('Enter the number of rows : '))
for i in range(1,a):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
for i in range(a-2,0,-1):
    for  j in range(i):
        print('*',end=' ')
    print()

    