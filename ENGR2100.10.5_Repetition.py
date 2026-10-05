#10.5 -- No lab this week -> exam :0
#loopy doopy day
#while loops and for loops with nested loops 

# a robot shoul dmove if the battery level is greater  than 20%

batt = float(input("What is the battery level? "))
while batt >= 20:
    if batt >= 20: 
        print("move")
    batt = batt-10
else:
    print("stop")

# use a while loop to count 1-10

count = 1
while count <= 10:
    print(count, end=" ")
    count += 1
print(f"\nDone counting. \nCount is now {count}")

#wrote a program that produces a conversion from c to f ranging from 5-30c in increments of 2.5c as a table

print("\n Celsius   Fahrenheit")
print("--------   ----------")
C = 5
F = (C * 9/5) + 32
while C<=30:
    print(f"{C:>7.1f}   {F:>10.1f}")
    C += 2.5
    F = (C * 9/5) + 32

#weather ballon altitude and velocity

ti = float(input("\n Enter initial time (hours): "))
tf = float(input("Enter final time (hours): "))
tinc = float(input("Enter the increment (hours): "))
print("\n Time (hours)  Altitude (m)  Velocity (m/s)")
while ti <= tf:
    alt = -.12*(ti**4)+12*(ti**3)-380*(ti**2)+4100*ti+220
    vmph= -0.48*(ti**3)+36*(ti**2)-760*ti+4100
    vms = vmph/3600
    print(f"{ti:>7.1f}   {alt:>14.1f}   {vms:>12.5f}")
    ti += tinc
