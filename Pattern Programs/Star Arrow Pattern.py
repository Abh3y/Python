'''
* 
 * * 
  * * * 
   * * * * 
  * * *
 * *
*

'''
a = int(input('Enter the number of rows: '))

# Upper part of the pattern (increasing stars with spaces)
for i in range(1, a):
    print(' ' * (i - 1), end='')  # Adding spaces at the start of each line incrementally.
    for j in range(1, i + 1):
        print('*', end=' ')
    print()  # Move to the next line

# Lower part of the pattern (decreasing stars without spaces)
for i in range(a - 2, 0, -1):
    print(' ' * (i - 1), end='')  # Adding spaces at the start of each line
    for j in range(1, i + 1):
        print('*', end=' ')
    print()  # Move to the next line
