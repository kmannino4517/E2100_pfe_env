#selection, repetition, if/else

#find the square root of a number if it is positive
#otherwise display error message

import math

print("Let's take a square root!")
num = float(input("Enter a number: "))

if num > 0:
    sqrt = math.sqrt(num)
    print()
    print(f"Square root of {num} is {sqrt:.3f}!")
else:
    print(f"\n {num} is not positive!!!")

#Write a program that converts temperature in fahrenheit to celcsius or celsius to fahrenheit. the user enters f if the input is in fahrenheit and c if the input is celsius
#inputs: temperature (temp_i) (#), character (char) (f or c)
#outputs: temperature (temp_n) (#)
#formulas: f= (9/5*c)+32 c=5/9*(f-32)
#assumptions: input temperature is in f or c

print("Let's convert some temperatures!")
temp_i = float(input("Enter your temperature as a number: "))
char = input("Enter F if your temperature is in Fahrenheit and C if your temperature is in Celsius: ")
f= (9/5*temp_i)+32 #temp in f
c= 5/9*(temp_i-32) #temp in c
if char.upper() == "F":
    print(f"Temperature entered is {temp_i} F")
    temp_n = c
    print(f"Temperature is {temp_n:.1f} C")
elif char.upper() == "C":
    print(f"Temperature is {temp_i} C")
    temp_n = f
    print(f"Temperature is {temp_n:.1f} F")
else:
    print("It's not Celsius or Fahrenheit... Try again.")

#calculating classes based on credits
cred = int(input("Enter your number of credits: "))
if cred < 32:
    print("Freshman")
elif cred < 64:
    print("Sophomore")
elif cred < 96:
    print("Junior")
else:
    print("Senior")
print(f"You have {cred} credits.")