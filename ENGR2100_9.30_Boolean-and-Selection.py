#selection continued and boolean

#AND = 0, 0 = 0 0, 1 =0 1, 0 =0 1,1=1
#OR = 0,0 = 0 0,1 = 1 1,0 = 1 1,1=1
#NOT = 1 =0 0=1

plugged_in = True #make sure True & False are capitalized
batt = 89

if plugged_in: #with booleans, you don't need to check == True
    print("plugged in...")
    if batt < 80:
        print("Charging...")
    else:
        print("Not charging...")
else:
    print("Not plugged in...")

#robot simulator
import random
import math

Name = input("enter robot name")
weight = float(input("enter weight"))
temp = float(input("Enter temperature"))
xi = float(input("Enter x position"))
yi = float(input("Enter y position"))
obj_x = float(input("Enter object x position"))
obj_y = float(input("Enter object y position"))
batt_i = 100
safe_dist = 50
batt_min = 20

v1 = random.uniform(2.0,5.0) #move 1 speed
v2 = random.uniform(2.0,5.0) #move 2 speed
theta1 = random.uniform(0.0,360.0) #move 1 angle
theta2 = random.uniform(0.0,360.0)#move 2 angle
s1 = random.uniform(5.0,10.0) #move 1 time
s2 = random.uniform(5.0,10.0) #move 2 time
p1 = random.uniform(1.0,6.0) #move 1 power
p2 = random.uniform(1.0,6.0) #move 2 power

print(f"Move 1 speed: {v1:.2f} angle: {theta1:.2f} time: {s1:2f} power: {p1:2f}")

#calcumilate

#energy and displacement

E1 = p1*s1
dx1 = xi-obj_x
dy1 = yi-obj_y
disp1 = math.hypot(dx1,dy1)
x1 = (s1*v1*math.cos(math.radians(theta1)))+xi
y1 = (s1*v1*math.sin(math.radians(theta1)))+yi
d1 = math.hypot((x1-xi),(y1-yi))
E2 = p2*s2
dx2= x1-obj_x
dy2 = y1-obj_y
disp2 = math.hypot(dx2,dy2)
x2= (s2*v2*math.cos(math.radians(theta2)))+x1
y2 = (s2*v2*math.sin(math.radians(theta2)))+y1
d2=math.hypot((x2-x1),(y2-y1))
batt1 = batt_i - E1
batt2 = batt1 - E2
print(f"Move 1\n energy consumption: {E1:>20.2f} \n displacement: {disp1:>20.2f}")

if disp1 > safe_dist and batt_i-E1>batt_min:
    print("Move 1 Succeeded")
    print(f"Move 1 Data \n Distance Travelled: {d1:<20.2f} \n Coordinate Placement: ({x1:2f},{y1:2f}) \n Battery Level: {batt1:2f}%")
    if disp2 > safe_dist and batt1-E2>batt_min:
        print(f"Move 2 Data \n Distance Travelled: {d2:<20.2f} \n Coordinate Placement: ({x2:2f},{y2:2f}) \n Battery Level: {batt2:2f}%")