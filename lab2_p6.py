# Lab 2, Part 6
# convert a sensor reading from m to km m
# for example, sensor = 13678m or 13km 678m
sensor = int(input("Enter the sensore reading (m): "))

#previously: kilometers = sensor / 1000
kilometers = sensor // 1000
meters = sensor % 1000          # % means reaminder

print(f"distance = {kilometers}km {meters}m")