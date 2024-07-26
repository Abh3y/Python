a=int(input('Enter the nth number '))
if a==1:
    print('Insert number greater than 1')
else:
    print('Prime numbers from 1 to',a,'are : ')
for i in range(2,a+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')

        

