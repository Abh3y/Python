'''
A 
B B 
C C C 
D D D D 
E E E E E
F F F F F F

'''
a=int(input('Enter the number of row : '))
b=65 # 65 is fpr alphabet A.
for i in range(1,a+1):
    for j in range(1,i+1):
        n=chr(b) # chr() is used to conver the ascii value 65 to its particular alphabet.
        print(n,end=' ')
    b=b+1 # This increment is used to print next alphabet.
    print()
    