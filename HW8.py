#Name: Neely Nabors
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library
import random

#2. print "Hello World!"
print("Hello World!")

#3. Create three different variables that each randomly generate an integer between 1 and 10
one = random.randint(1, 10)
two = random.randint(1, 10)
three = random.randint(1,10)

#4. Print the three variables from #3 on the same line.
print(one, two, three)

#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
one_sum = one + 2
two_sum = two - 4
three_sum = three * 1.5

#6. Print each result from #5 on the same line.
print(one_sum, two_sum, three_sum)

#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
four_var = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

#8. Sort the list in #7 and print it.
four_var.sort()
print(four_var)

#9. Add together the highest three numbers in the list from #7 and print the result.
highest_three = four_var[1] + four_var[2] + four_var[3]
print(highest_three)

#10. Create a list with 5 names of other students in this class and print the list.
names = ["Lila", "Echo", "Cruz", "Ethan", "Gavin"]
print(names)

#11. Shuffle the list in #10 and print the list again.
random.shuffle(names)
print(names)

#12. Print a random choice from the list of names from #10.
name_choice = random.choice(names)
print(name_choice)