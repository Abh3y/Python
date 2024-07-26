a=int(input('Enter the number : '))
b=a
n=0
while a!=0:
    s=a%10
    n=n+(s**3)
    a=a//10
print(n)
if b==n:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')
