# Python program that accepts a string and calculates the number of digits and letters.
a=input('Enter the string : ')
s=0
n=0
for i in a:
    if i.isdigit(): # isdigit() function is used to detect whether the given string is a digit or not.
        n=n+1
    elif i.isalpha(): # isalpha() function is used to detect whether the given string is a letter or not.
        s=s+1
print('Total number of letters : ',s)
print('Total number of digits are ',n)