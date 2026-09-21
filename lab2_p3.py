# Lab 2, Part 3
# convert temperature from C to F and print both temperatures

celsius = float(input("Enter temperature in Celsius: ")) 
fahrenheit = celsius * 9 / 5 + 32 

print()
print(f"Temperature: {celsius:.1f} C") 
#previously: print(f"Temperature: {fahrenheit.1f} F")
print(f"Temperature: {fahrenheit:.1f} F")