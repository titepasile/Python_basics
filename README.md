# Python_basics
## Important links
For all internal Python modules:
-  https://docs.python.org/3/py-modindex.html
-  

## Operations
Parentheses > Exponentiation > Multiplication/Division/Integer Division/Modulo > Addition/Subtraction

Now that you've mastered the basics like addition (+), subtraction (-), multiplication (*), division (/), and integer division (//), it's time to dive a little bit deeper.

In today's lesson, we'll introduce two powerful operators: exponentiation (**) and modulo (%). These tools are especially useful in everything from game development to cryptography, and once you learn how to use them, you'll wonder how you ever lived without them.
Exponentiation (**)

The exponentiation operator allows you to raise a number (the base) to the power of another number (the exponent). Think of it like repeated multiplication.

Syntax

result = base ** exponent

Examples

print(2 ** 3)  # Output: 8, because 2  2  2 = 8
print(5 ** 0)  # Output: 1, any number to the power of 0 is 1
print(10 ** 2) # Output: 100

⚠️ Python can handle large exponents, but be cautious: the result can grow very quickly and consume a lot of memory.

Let's see some practical use cases of this operator:

Squares and Cubes

You can easily calculate squares (power of 2) and cubes (power of 3) of numbers using **.

print(5 ** 2)  # Output: 25 → 5 squared
print(2 ** 3)  # Output: 8  → 2 cubed
print(10 ** 2) # Output: 100 → 10 squared

Handy when dealing with geometry, physics, or just quick math tricks.

Growing Numbers Quickly

Exponentiation grows numbers really fast!

print(2  5)  # Output: 32
print(3  4)  # Output: 81
print(10 ** 6) # Output: 1000000

This comes in useful when working with large values like powers of 10 (e.g. "a million" is 10 ** 6) or understanding exponential growth.

Area and Volume Formulas

You’ll often see powers in math and physics formulas.

    Area of a square = side²

    Volume of a cube = side³

side = 4 
print(side ** 2)  # Area: 16 
print(side ** 3)  # Volume: 64

These are simple applications where ** makes your code much cleaner and easier to read.
Modulo (%)

The modulo operator gives you the remainder of a division operation.

Syntax

remainder = dividend % divisor

Examples

print(10 % 3)  # Output: 1, because 10 = 3 * 3 + 1
print(14 % 5)  # Output: 4
print(21 % 7)   # Output: 0, since 21 is divisible by 7

The modulo operator is great when you need to:

Check if a number is even or odd

Let’s see what happens when we divide some numbers by 2 and print the remainder:

print(4 % 2)  # Output: 0  
print(7 % 2)  # Output: 1  
print(10 % 2) # Output: 0  
print(13 % 2) # Output: 1 

If the result is 0, the number is even. If it’s 1, it’s odd.

Wrap values around in games or cyclic tasks

Imagine you're moving through 3 levels in a game: 0, 1, 2. After 2, you want to start again from 0.

print((0 + 1) % 3)  # Output: 1 
print((1 + 1) % 3)  # Output: 2 
print((2 + 1) % 3)  # Output: 0 (wraps around!) 
print((3 + 1) % 3)  # Output: 1

This is a simple way to make numbers repeat in a cycle — perfect for menus, animations, or timed events.

Periodic patterns

Want to see which numbers are multiples of 3?

print(3 % 3)   # Output: 0 
print(6 % 3)   # Output: 0 
print(9 % 3)   # Output: 0 
print(10 % 3)  # Output: 1 
print(11 % 3)  # Output: 2

When the remainder is 0, the number is divisible by 3. Try printing % results for more numbers and see if you can spot the pattern!
A Quick Note on Negative Numbers

Both operators behave a little differently when negative numbers are involved.

Exponentiation

print(-2 ** 2)  # Output: -4 (not 4!)
print((-2) ** 2) # Output: 4

Why? Because Python applies exponentiation before negation. So −2∗∗2−2∗∗2 is interpreted as −(2∗∗2)−(2∗∗2).

Modulo

print(-10 % 3)  # Output: 2
print(10 % -3)  # Output: -2

Python ensures the result of % always has the same sign as the divisor.
Summary

In this lesson, you’ve learned:

    ∗∗∗∗ lets you raise numbers to a power.

    %% helps you find the remainder in division.

    Python's operator precedence and sign behavior can impact your results.

Keep experimenting, and don’t worry if you make mistakes — that’s part of the learning process!