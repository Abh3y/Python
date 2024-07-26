'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6

'''
a=int(input('Enter the number of rows : '))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i,end=' ') 
    print()