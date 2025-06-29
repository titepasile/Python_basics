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

numbers = range(1, 100)

for number in  numbers:
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)
    
