#Assignment 1, Question 1
#Koda Mannino
#9.21.2026
PI=3.14159

diameter=float(input("Enter the diameter (m): "))
length=float(input("Enter the length (m): "))

density=7850 #kg/m^3

radius=diameter / 2
volume=PI * radius**2 * length
mass = density * volume

print()
print(f"The mass is {mass:.2f} kg")