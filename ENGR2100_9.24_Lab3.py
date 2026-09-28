#Lab 3 -- Operations and Selection

import math

v_i = float(input("Enter initial velocity: ")) #initial velocity
theta =  (float(input("Enter launch angle: "))) #launch angle
target = float(input("Enter target distance: ")) #target  distance
theta_r = math.radians(theta)
g = 9.81 #gravitational acceleration

#getting components

v_x = v_i * math.cos(theta_r) #x component
v_y = v_i * math.sin(theta_r) #y component

#flight details

h_max = v_y**2/(2*g) #max height
t_up = v_y/g #time up 
t_total = 2*t_up #total time
R = v_x*t_total #x distance
dR=R-target #distance from target

print()
print()
print("Projectile Launch Analysis")
print("--------------------------")
print(f"Initial Velocity: {v_i:>6.2f} m/s")
print(f"Launch Angle: {theta:>10.2f} degrees")
print(f"Target Distance: {target:>7.2f} m")

print()
print("Velocity Components")
print("-------------------")
print(f"Horizontal Velocity: {v_x:>5.2f} m/s")
print(f"Vertical Velocity: {v_y:>7.2f} m/s")

print()
print("Flight Analysis")
print("---------------")
print(f"Maximum Height: {h_max:>14.2f} m")
print(f"Time to Maximum Height: {t_up:>5.2f} s")
print(f"Flight Time: {t_total:>16.2f} s")
print(f"Horizontal Range: {R:>12.2f} m")
print(f"Distance from Target: {dR:>7.2f} m")

if dR != 0:
    print("WARNING: The package did not reach the target!!!")
