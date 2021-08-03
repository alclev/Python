import math
while True: 
    angle= input("Angle Measure (degrees) : ")
    vi= input("Initial Velocity (m/s): ")
    output = int(math.cos(math.radians(float(angle)))*float(vi)*((2*math.sin(math.radians(float(angle)))*float(vi))/9.8))
    print("Range= " + str(output) + " meters\n")
    print("___________________________________")
 
