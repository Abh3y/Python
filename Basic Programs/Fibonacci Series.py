# Define the number of terms in the Fibonacci series you want to print
n=int(input('Enter the last number to which you want the fibonacci series : '))

# The first two terms of the Fibonacci series
a, b = 0, 1
# This loop will run num_terms times
for i in range(n):
    # Print the current term
    print(a)

    # Calculate the next term by adding the last two terms
    next = a + b

    # Update the last two terms
    a = b
    b = next