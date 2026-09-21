#creating varibales lol
#length = 10.0
#width = 5.0
#area = length * width
#print("area is", length * width, "in^2")
#print(area, "in^2")
#standard input
#l = float(input("enter length:"))
#w = float(input("enter width:"))
#a= l * w
#ans = float(input("enter area:"))
#boolean = a == ans
#if boolean: 
#    print("correct")
#else: 
#    print("incorrect; area is ", a)
#formatted strings
#name = "John Harvard"
#Grade = 54.88792
#print("Student", name, "\n" "Grade is", Grade)
#print(f"Student {name}\nGrade is {Grade}")
#print(f"Student {name}\nGrade is {Grade:.2f}")
#tablessss
#z1= "ur mom"
#y1= 500
#z2= "slime"
#y2= 30
#z3= "Clemson"
#y3= 12
#print(f"Name          Weight \n ----------------\n {z1:<10} {y1}\n {z2:<10} {y2}\n {z3:<10} {y3}")
# in class excercise medication deliveraty and velocity and acceleration

#A medication pump is designed to deliver medication at a rate of .02 mg/kg/hr. Display the dose needed given a weight.
W = float(input("Patient's Weight in kilograms: "))
dose = W * .02
print(f"\n \n The dose for this patient is {dose} mg/hr")
input("Press enter to continue")
#Calculate and display the velocity and acceleration of an aircraft after a change in input power. Velocity and acceleration is calculated using an equation.
t=float(input("Enter time in seconds: "))
v=.00001*t**3 - .00488*t**2 +.75795*t +181.3566
a=3.0 - .000062*v**2
print(f"\n ---------------------------------------- \n {'Velocity':<25} {v:>10.3f} m/s \n {'Acceleration':<25} {a:>8.3f} m/s^2 \n ----------------------------------------")