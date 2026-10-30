import random

print("Which Stranger Things characters are you most related to?")



Age = int(input("Enter your age: "))



if Age < 16:
    print("You are like Mike, Dustin, Lucas, Will, Max, and Eleven")
elif Age > 16 and Age < 18:
    print("You are like Steve, Robin, Nancy, and Jonathan")
else:
    print("You are like Hopper, Joyce, Murray, and Dr. Brenner")
print("Okay, now for your personality")

personality = input("Personality: ")

if personality == "Introvert":
    print("you are like hopper")
else:
    print("You are like Dustin, Robin, Hopper, Nancy, Steve")
print("Nice! Now lets do your eye color.")

eye = input("eye color: ")

if eye == "brown":
    print("you are like Eleven, Mike, Lucas, Joyce")
else:
    print("You are like Max, Hopper, Nancy, and Will")
print("Thank you! Now go rewatch stranger things")

