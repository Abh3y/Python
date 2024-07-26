'''
10
10 8
10 8 6
10 8 6 4
10 8 6 4 2

'''
rows = int(input("Enter the number of rows: "))  
lastnum = 2 * rows
even = lastnum

#Outer for loop to handle number of rows  
for i in range(1, rows+1):  
  even = lastnum
  for j in range(i): 
    print(even, end=" ")     
    even -= 2  
  print()