a=int(input('Enter the number : '))
if a==1:
    print('Not prime number')
else: 
    for i in range(2,a):
        if a%i==0:
            print('Not prime number')
            break
    else:
        print('Prime number')
        
