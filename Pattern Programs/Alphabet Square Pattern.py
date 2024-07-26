'''
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E

'''
a=int(input('Enter the rows : '))
for i in range(1,a+1):
    for j in range(0,a):
        s=chr(ord('A')+j)
        print(s,end=' ')
    print()
        
    