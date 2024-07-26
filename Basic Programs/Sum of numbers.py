# a=int(input('Enter the starting number : '))
# b=int(input('Enter the last number : '))
# i=a+1
# print(a, end=' ')
# while i<=b:
#     a=a+i
#     i=i+1
#     print('+',i-1,end=' ')
# print()
# print('Total is : ',a)
 
a=int(input('Enter the starting number : '))
b=int(input('Enter the last number : '))
sum=0
print(a,end=' ')
for i in range(a,b+1):
   sum=sum+i
   print('+',i,end=' ')
print()
print('Total is : ',sum)
