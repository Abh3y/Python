'''
         * 
        * * 
       * * * 
      * * * * 
     * * * * *
    * * * * * *

'''
a = int(input("Enter the number of rows : "))  
for i in range(1, a+1):  
    for j in range(a,0,-1):  
      if j > i:
        print('',end=' ') 
      else:
        print('*', end=' ')
    print()