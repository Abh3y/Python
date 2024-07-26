a=int(input('Enter the number : '))
b=a
print(a,end=' ')
for i in range(a-1,0,-1):
    print('*',i,end=' ')
    s=a*i
    a=s
print()
print('Factorial of ',b,'is : ',s)