# Lab 2, Part 4
# calculate and display the distance travelled

speed = float(input("Enter robot speed (m/s): ")) 
seconds = float(input("Enter travel time (s): ")) 

#previously: distance = speed x seconds
distance = speed * seconds 

print(f"The robot traveled {distance:.2f} meters.")