#Robot Simulator 9.14
#import math


#x = 100
#y = 50
#s = 4.5
batt0 = 100
#name = "Jiminy"
#w = 12.5
#t = 23.4
#print(name, "Values: ", "Coordinates:", x, ",", y, "Speed:", s, "m/s", "Battery:", batt, "%", "Weight:", w, "kg", "Temperature:", t, "C") 9.14 work
#Name = input("Enter robot name: ")
#x1 = float(input("Enter x coordinate: "))
#y1 = float(input("Enter y coordinate: "))
#S = float(input("Enter speed: "))
#Battery = float(input("Enter battery percentage: "))
#Weight = int(input("Enter weight: "))
#Temperature = float(input("Enter temperature: "))
#print(f"\n \n {Name} \n Values: \n Coordinates: {x1:.1f}, {y1:.1f}, \n Speed: {S:.2f} m/s, \n Battery: {Battery:.0f} %, \n Weight: {Weight} kg \n Temperature: {Temperature:.1f} C")

#adding robot distance and displacement

#x2 = float(input("Enter new x coordinate: "))
#y2 = float(input("Enter new y coordinate: "))

#dist=abs((x2-x1)+(y2-y1))
#disp=math.hypot(x2-x1, y2-y1)

#print(f"\n--------------------------\n {'Distance:':<10} {dist:>10.2f} m \n {'Displacement:':<10} {disp:>7.2f} m \n --------------------------")
import math 
name = input("Enter name: ")
weight = float(input("enter weight: "))
temp = float(input("enter temperature: "))
x_o = float(input("enter initial x position"))
y_o = float(input("enter initial y position"))

print("gathering data for move one")

v1 = float(input("enter velocity"))
theta1 = math.radians(float(input("enter angle: ")))
t1 = float(input("enter the time"))
p1 = float(input("enter the power"))

print("gathering data for move two")

v2 = float(input("enter velocity"))
theta2 = math.radians(float(input("enter angle: ")))
t2 = float(input("enter the time"))
p2 = float(input("enter the power"))

d1= v1 * t1
x1 = d1 * math.cos(theta1) +x_o
y1 = d1 * math.sin(theta1) +y_o
e1 = p1*t1
batt1= batt0-e1
d2 = v2 * t2
x2 = d2 * math.cos(theta2) +x1
y2 = d2 * math.sin(theta2) +y1
e2=p2*t2
batt2= batt1-e2
d=d1+d2
dx=x2-x_o
dy=y2-y_o
disp=math.hypot(dx,dy)

print("General Information")
print("___________________")
print(f"{"Robot Name":<20}{name} \n {"Robot Weight":<20} {weight} \n {"Temperature":<20}{temp}")
print()
print(f"Starting position: ({x_o:.1f},{y_o:.1f})")
print(f"{"Battery Level":<20}{batt0} %")

print("Move 1")
print("_________")
print(f"{"Speed":<10}{v1} m/s")
print(f"{"Angle":<10}{math.degrees(theta1)} degrees")
print(f"{"Power":<10}{p1} W")
print(f"{"Distance":<10}{d1} m")
print(f"{"New Postiion":<15} ({x1:.1f},{y1:.1f})")
print(f"{"Energy":<10}{e1} J")
print(f"{"Battery":<10}{batt1} %")

print()

print("Move 2")
print("_________")
print(f"{"Speed":<10}{v2} m/s")
print(f"{"Angle":<10}{math.degrees(theta2)} degrees")
print(f"{"Power":<10}{p2} W")
print(f"{"Distance":<10}{d2} m")
print(f"{"New Postiion":<15} ({x2:.1f},{y2:.1f})")
print(f"{"Energy":<10}{e2} J")
print(f"{"Battery":<10}{batt2} %")

print()

print("Overall Results")
print(f"Total distance moved = {d:.1f} m")
print(f"Displacement = {disp:.1f} m")
print(f"Final position: ({x2:.1f},{y2:.1f})")
print(f"Battery level = {batt2} %")