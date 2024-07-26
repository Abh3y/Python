a=int(input('Enter the first number : '))
b=int(input('Enter the last number : '))
print('The even numbers are : ',end=' ')
for i in range(a,b+1):
    if i%2==0:
        print(i,end=' ')
print()
print('Odd Numbers are : ',end=' ')
for j in range(a,b+1):
    if j%2!=0:
        print(j,end=' ')