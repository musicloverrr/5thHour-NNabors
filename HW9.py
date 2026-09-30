#Name: Neely Nabors
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World!")

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
st_dictionary = {
    "tv show" : "stranger things",
    "character" : "Hopper",
    "seasons" : [1,2,3]
}

#3. Print the keys of the dictionary from #2.
print(st_dictionary.keys())

#4. Print the values of the dictionary from #2
print(st_dictionary.values())

#5. Print one of the three numbers from the list by itself
print(st_dictionary["seasons"][1])

#6. Using the update function, add a fourth key to the dictionary and give it a value.
st_dictionary.update({"monster" : "Demogorgon"})

#7. Print the entire dictionary from #2 with the updated key and value.
print(st_dictionary)

#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
my_fifth_hour_class = {
    "student_1" : {
        "Name" : "Echo",
        "Grade" : 11,
        "Sport" : True,
    },
    "student_2" : {
        "Name" : "Lila",
        "Grade" : 9,
        "Sport" : False,
    },
    "student_3" : {
        "Name" : "Cruz",
        "Grade" : 9,
        "Sport" : False,
    },
}
#9. Print the names of all three classmates on the same line.
print(my_fifth_hour_class["student_1"]["Name"],my_fifth_hour_class["student_2"]["Name"],my_fifth_hour_class["student_3"]["Name"])

#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
my_fifth_hour_class.pop("student_3")
print(my_fifth_hour_class)