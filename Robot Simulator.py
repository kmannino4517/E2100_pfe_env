#Robot Simulator 9.14
import math


x = 100
y = 50
s = 4.5
batt = 85
name = "Jiminy"
w = 12.5
t = 23.4
#print(name, "Values: ", "Coordinates:", x, ",", y, "Speed:", s, "m/s", "Battery:", batt, "%", "Weight:", w, "kg", "Temperature:", t, "C") 9.14 work
Name = input("Enter robot name: ")
x1 = float(input("Enter x coordinate: "))
y1 = float(input("Enter y coordinate: "))
S = float(input("Enter speed: "))
Battery = float(input("Enter battery percentage: "))
Weight = int(input("Enter weight: "))
Temperature = float(input("Enter temperature: "))
print(f"\n \n {Name} \n Values: \n Coordinates: {x1:.1f}, {y1:.1f}, \n Speed: {S:.2f} m/s, \n Battery: {Battery:.0f} %, \n Weight: {Weight} kg \n Temperature: {Temperature:.1f} C")

#adding robot distance and displacement

x2 = float(input("Enter new x coordinate: "))
y2 = float(input("Enter new y coordinate: "))

dist=abs((x2-x1)+(y2-y1))
disp=math.hypot(x2-x1, y2-y1)

print(f"\n--------------------------\n {'Distance:':<10} {dist:>10.2f} m \n {'Displacement:':<10} {disp:>7.2f} m \n --------------------------")