# Lab 2, Part 5
# calculate and display the power dissipated in an electrical circuit

voltage = float(input("Enter the voltage (V): "))
current = float(input("Enter the current (A): "))

power = voltage * current

print()
#previously: print("power = power W")
print(f"power = {power} W")