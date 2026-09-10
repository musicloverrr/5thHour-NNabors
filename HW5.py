#Name: Neely Nabors
#Class: 5th Hour
#Assignment: HW5

#1. Print Hello World!
print("Hello World!")

#1. Create a list with 5 strings containing 5 different names in it.
first_name_list = ["Naruto", "Sasuke", "Sakura", "Kakashi", "Shikamaru"]

#2. Append a new name onto the Name List.
first_name_list.append(input("Insert Person to List: "))

#3. Print out the 4th name on the list.
print(first_name_list)
print(first_name_list[3])

#4. Create a list with 4 different integers in it.
num_list = [1, 3, 8, 11]

#5. Insert a new integer into the 2nd spot and print the new list.
num_list.insert(1, 15)
print(num_list)

#6. Sort the list from lowest to highest and print the sorted list.
num_list.sort()
print(num_list)

#7. Add the 1st three numbers on the sorted list together and print the sum.
num_list_sum = num_list[0] + num_list[1] + num_list[2]
print(num_list_sum)

#8. Create a list with two strings, two variables, and too boolean values.
second_list = ["Hinata", "Neji", 25, 90, True, False]
print(second_list)

#9. Create a print statement that asks the user to input their own index value for the list on #8.

print(second_list[(int(input("Insert Index Value to List: ")))])