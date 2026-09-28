#Assignment 1, Question 1
#Koda Mannino
#9.21.2026
#PI=3.14159

#diameter=float(input("Enter the diameter (m): "))
#length=float(input("Enter the length (m): "))

#density=7850 #kg/m^3

#radius=diameter / 2
#volume=PI * radius**2 * length
#mass = density * volume

#print()
#print(f"The mass is {mass:.2f} kg")
#9.23 work
O = 15.9994 #oxygen molecular weight
C = 12.011 #carbon molecular weight
N = 14.0674 #nirtogen molecular weight
S = 32.066 #sulfur molecular weight
H= 1.00794 #hydrogen molecular weight
print("Alanine molecular components")
O_A = float(input("Enter the number of oxygen atoms in Alanine: "))
C_A = float(input("Enter the number of carbon atoms in Alanine: "))
N_A = float(input("Enter the number of nitrogen atoms in Alanine: "))
S_A = float(input("Enter the number of sulfur atoms in Alanine: "))
H_A = float(input("Enter the number of hydrogen atoms in Alanine: "))

#Alanine molecular weight check
A_o = O_A * O #weight of oxygen in alanine
A_c = C_A * C #weight of carbon in alanine
A_n = N_A * N #weight of nitrogen in alanine
A_s = S_A * S #weight of sulfur in alanine
A_h = H_A * H #weight of hydrogen in alanine
print(f"{A_h} alanine hydrogen")
print(f"{A_s} alanine sulfur")
print(f"{A_n} alanine nitrogen")
print(f"{A_c} alanine carbon")
print(f"{A_o} alanine oxygen")
A = A_o + A_c + A_n +A_s + A_h #weight of alanine
print(f"Alanine's molecular weight is {A} g/mol")

print("Glutamine molecular components")
O_G = float(input("Enter the number of oxygen atoms in Glutamine: "))
C_G = float(input("Enter the number of carbon atoms in Glutamine: "))
N_G = float(input("Enter the number of nitrogen atoms in Glutamine: "))
S_G = float(input("Enter the number of sulfur atoms in Glutamine: "))
H_G = float(input("Enter the number of hydrogen atoms in Glutamine: "))

#Glutamine molecular weight check
G_o = O_G * O #weight of oxygne in glutamine
G_c = C_G * C #weight of carbon in glutamine
G_n = N_G * N #weight of nitrogen in glutamine
G_s = S_G * S #weight of sulfur in glutamine
G_h = H_G * H #weight of hydrogen in glutamine
print(f"{G_h} alanine hydrogen")
print(f"{G_s} alanine sulfur")
print(f"{G_n} alanine nitrogen")
print(f"{G_c} alanine carbon")
print(f"{G_o} alanine oxygen")
G = G_o + G_c + G_n +G_s + G_h #weight of glutamine
print(f"Glutamine's molecular weight is {G} g/mol")
print("Tryptophan molecular components")
O_T = float(input("Enter the number of oxygen atoms in Tryptophan: "))
C_T = float(input("Enter the number of carbon atoms in Tryptophan: "))
N_T = float(input("Enter the number of nitrogen atoms in Tryptophan: "))
S_T = float(input("Enter the number of sulfur atoms in Tryptophan: "))
H_T = float(input("Enter the number of hydrogen atoms in Tryptophan: "))
#Tryptophan molecular weight check
T_o = O_T * O #weight of oxygen in tryptophan
T_c = C_T * C #weight of carbon in tryptophan
T_n = N_T * N #weight of nitrogen in tryptophan
T_s = S_T * S #weight of sulfur in tryptophan
T_h = H_T * H #weight of hydrogen in tryptophan
print(f"{T_h} alanine hydrogen")
print(f"{T_s} alanine sulfur")
print(f"{T_n} alanine nitrogen")
print(f"{T_c} alanine carbon")
print(f"{T_o} alanine oxygen")
T = T_o + T_c + T_n +T_s + T_h #weight of tryptophan
print(f"Tryptophan's molecular weight is {T} g/mol")
print()
print("Amino Acid Weight")
print("__________________")
print(f"Alanine {A:>10.2f}")
print(f"Glutamine {G:>8.2f}")
print(f"Tryptophan {T:>7.2f}")

#part 3
import math
x1= float(input("Enter x1: "))
y1= float(input("Enter y1: "))
x2= float(input("Enter x2: "))
y2= float(input("Enter y2: "))

dx=x2-x1 #change in x
dy=y2-y1 #change in y

g=dy/dx #=y2-y1/x2-x1

d=math.hypot(dx,dy) #=pythag theorem

print()
print(f"Coordinates are ({x1},{y1}) and ({x2},{y2})")
print(f"Gradient = {g}")
print(f"Distance = {d}")