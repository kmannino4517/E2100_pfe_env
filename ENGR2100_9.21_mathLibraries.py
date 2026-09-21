#MATH STUFF
import math


math.sqrt(16) #square root
math.log(100) #log base 10
math.log(100,2) #log base 2
math.log(100,math.e) #natural log
#trig uses radians!
math.sin(90) #sine
math.cos(90) #cosine
math.tan(90) #tangent
math.acos(1) #arccosine
math.atan(90) #arctangent
math.cos(math.radians(90)) #cosine in degrees
math.pi #pi
math.e #e
math.degrees(math.pi) #convert radians to degrees
math.fabs(-5) #absolute value

#a velocity vector has components vx=12 m/s and vy=5m/s display magintude and direction of the vector
vx=12
vy=5 
mag=math.hypot(vx,vy) #magnitude
dir=math.degrees(math.atan(vy/vx)) #direction
print(f" Velocity in x is {vx} \n Velocity in y is {vy} \n Magnitude is {mag:.2f} \n Direction is {dir:.2f} degrees")

#calculate the magnitude and direction of a force given the x and y components
fx = float(input("enter the x component (N) "))
fy = float(input("enter the y component (N)  "))
fmag=math.hypot(fx,fy)
fdir=math.degrees(math.atan2(fy,fx))
print(f"Force is {fmag:.2f} N at {fdir:.2f} degrees")

#DC motor energy in Waytt-hours

V=float(input("Enter voltage (V): "))
I= float(input("Enter current (A): "))
t=float(input("Enter time (s): "))

E_Wh=V*I*t/3600

P=V*I
E_j=P*t

print(f"Power = {P:.2f} W")
print(f"Energy = {E_j:.2f} J = {E_Wh:.2f} Wh")