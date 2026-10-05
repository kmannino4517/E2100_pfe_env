#Lab 4
import math
print("Let's see if you can lift that load!")

g = 9.81 #acceleration due to gravity

m = float(input("Enter mass (kg): "))
theta = float(input("Enter the sling angle (degrees): "))
theta_r = math.radians(theta)
d = float(input("Enter the diamter (mm): "))
d_m = d/1000
ro_max = float(input("Enter maximum allowable sling stress (MPa): "))
m_cmax = float(input("Enter the maximum capacity of the crane (kg): "))

W = m*g #weight
A = math.pi*d_m**2*.25 #sling cross sectional area
T = W/(2*math.sin(theta_r)) #vertical tension in sling
ro_Pa = T/A #stress in sling
ro_MPa = ro_Pa/10**6 #stress in sling, MPa
Tx = T*math.cos(theta_r) #Tension in X
Ty = T*math.sin(theta_r) #Tension in Y
FS = ro_max/ro_MPa #Factor of Safety

print(f"\nResults \n--------------")
print(f"Load Mass: {m:>20.2f} kg")
print(f"Load Weight: {W:>18.2f} N")
print(f"Sling Angle: {theta:>18.2f} degrees")
print(f"Sling Diameter: {d:>15.2f} mm")
print(f"Tension per sling: {T:>12.2f} N")
print(f"Sling area: {A:>19.6f} m^2")
print(f"Sling stress: {ro_MPa:>17.2f} MPa")
print(f"Allowable stress: {ro_max:>13.2f} MPa")
print(f"Factor of Safety: {FS:>13.2f}")
print(f"Horizontal Force: {Tx:>13.2f} N")
print(f"Vertical Force: {Ty:>15.2f} N")
print(f"Crane Capacity: {m_cmax:>15.2f} kg")
print(f"\nApproval Decision \n-------------")
if m>m_cmax or ro_MPa>ro_max or FS<3.0:
    print("LIFT NOT APPROVED")
    if m>m_cmax:
        print("Reason: Mass Exceeds Crane Capacity")
    if ro_MPa>ro_max:
        print("Reason: Stress Exceeds Sling Strength")
    if FS<2.0:
        print("Reason: Factor of Safety is Unsafe")
    elif FS<3.0:
        print("Reason: Factor of Safety is Marginal")
    print(f"\n \nSafety Classification \n------------------- \nSafety Classification: Unacceptable")
else: 
    print(f"LIFT APPROVED\n \nSafety Classification \n------------------- \nSafety Classification: Acceptable")