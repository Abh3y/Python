'''
   1
  23
 345
4567

'''
a=int(input('Enter the rows : '))
for i in range(1,a+1):
    for j in range(a-i):
        print(' ',end='')
    for k in range(i):
        print(i+k,end='')
    print()