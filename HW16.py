#Name: Neely Nabors
#Class: 5th Hour
#Assignment: HW16
import time

#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
#4. Add a and b together, then divide the sum by c. Print the result.
first = a + b
print(first / c)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print(round(first / c))
if first % 2 == 0:
    print("even")
else:
    print("odd")
#6. Create a list of five different random integers between 1 and 10.
num_list = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
#7. Print the 4th number in the list.
print(num_list[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
num_list.append(random.randint(1, 10))
print(num_list)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
num_list.sort()
print(num_list[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 100:
    print(i)
    i += i

#11. Create a list containing the names of five other students in the classroom.
names = ["Echo", "Lila", "Cruz", "Ethan", "Gavin"]
#12. Create a for loop that individually prints out the names of each student in the list.
for name in names:
    print(name)

#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for k in range(1, 100):
    if k % 10 == 0:
        break
    else:
        print(k)

#14. Free space. Do something creative. :)
for naruto in range(1, 100):
    if naruto % 2 == 0:
        print("Sasuke is goated")
    else:
        print("Naruto is goated")

