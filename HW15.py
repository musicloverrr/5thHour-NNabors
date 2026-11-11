#Name: Neely Nabors
#Class: 5th Hour
#Assignment: HW15
import random, time

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for i in range(5, 0, -1):
    print(i)
else:
    print("Hello World!")

#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for j in range(0, 30, 2):
    print(j)

#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for num in range(0, 30):
    if num % 3 == 0:
        continue
    print(num)

#4. Create a for loop that prints 5 different animals from a list.
animals = ["cat", "dog", "bunny", "bird", "tiger"]
for k in animals:
    print(k)

#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for word in input("Type in a word: ")[::-1]:
    print(word)

#6. Create a list containing 10 integers of your choice and print the list.
integers = [1, 11, 4, 45, 89, 6, 7, 81, 49, 38]
print(integers)

#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0


#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.

for num in integers:
    if num % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1
print(evenNumbers)
print(oddNumbers)

#9. Create a variable that asks the user for an integer and an empty integer variable.

x = int(input("Type in an integer and an empty integer variable: "))

y = 1



#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)

for n in range (1, x + 1):
    y *= n
    print(f"The factorial of {x} is {y}")


