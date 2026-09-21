#LUser enters solar powered system data, gives data about it
#panel area A = XX m^2
#solar irradiance G=XX W/m^2
#panel efficiency u_pan=XX % -> given as decimal
#system voltage V=XX V
#operating time t=XX h
#battery efficiency u_batt= XX% -> given as decimal

A = float(input("enter panel area (m^2): "))
G = float(input("enter solar irradiance (W/m^2): "))
u_pan = float(input("enter panel efficiency (as a decimal): "))
V = float(input("enter system voltage (V): "))
t = float(input("enter operating time (h): "))
u_batt = float(input("enter battery efficiency (as a decimal): "))

P_solar = A * G #solar panel incident
P_electrical = P_solar * u_pan # electrical power
I = P_electrical/V #panel current
E = P_electrical * t # energy produced
E_batt = E * u_batt # energy stored in battery

print(f" \n \n Solar Panel Information \n ---------------------- \n Incident Power: {P_solar:.1f} W \n Electrical Power: {P_electrical:.1f} W \n Current: {I:.1f} A \n Energy Produced: {E:.1f} J \n Energy Delivered: {E_batt:.1f} J")