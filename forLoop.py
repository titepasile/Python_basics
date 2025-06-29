# Write a program that does the following:
# Read two integers, a and b, from the user input. These numbers define the range [a, b] (inclusive).
# Find all numbers within this range (including a and b) that are divisible by 3.
# Calculate and print the mean (average) of these numbers.

# Read input values
a = int(input())
b = int(input())

# Initialize sum and counter
total = 0
count = 0

# Loop through the range [a, b]
for number in range(a, b + 1):
    if number % 3 == 0:
        total += number
        count += 1

# Calculate and print the mean
mean = total / count
print(mean) 

#--------------------------------------------------------------------------------------------------------
#Fizz Buzz
#

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    
