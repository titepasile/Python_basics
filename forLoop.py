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

#--------------------------------------------------------------------------------------------------------
#Speech generation
phone_number = input()

digits = ['zero', 'one', 'two',  'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for i in phone_number:
    if i == "0":
        print(digits[0])
    if i == "1":
        print(digits[1])
    if i == "2":
        print(digits[2])
    if i == "3":
        print(digits[3])
    if i == "4":
        print(digits[4])
    if i == "5":
        print(digits[5])
    if i == "6":
        print(digits[6])
    if i == "7":
        print(digits[7])
    if i == "8":
        print(digits[8])
    if i == "9":
        print(digits[9])

#--------------------------------------------------------------------------------------------------------
# We've stored a time value in the 24-hour format in a variable named hour. Your task is to convert this value to a 12-hour format and print the result.
hour = int(input())
print(12 if hour % 12 == 0 else hour % 12)

#--------------------------------------------------------------------------------------------------------
# Who doesn't want to be rich? So, let's invest some money.
# If you invest $x$x at an annual interest rate of r%r%, compounded yearly, the value of the investment aa, after yy years will be:
# a=x×(1+r100)ya=x×(1+100r​)y
# Let's say you have invested $1000$1000 at the yearly compound interest rate of 5%5%. What will be the value of the investment after 1010 years? Please complete the Python code below and print the answer only.
# Tip: Watch out for those parentheses—they're key to getting the right result!

x = 1000
r = 5
y = 10

a = x * (1 + r / 100) ** y
print(a)

#--------------------------------------------------------------------------------------------------------

