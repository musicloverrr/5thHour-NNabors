#Name: Neely Nabors
#Class: 5th Hour
#Assignment: SC3
import random
import time
#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.

num = 1

while num <= 100:
   if num % 3 == 0:
      time.sleep(0.4)
      print("Fizz")
   elif num % 5 == 0:
      time.sleep(0.4)
      print("Buzz")
   elif num % 3 == 0 and num % 5 == 0:
      time.sleep(0.4)
      print("FizzBuzz")
   else:
      print(num)

   num += 1
