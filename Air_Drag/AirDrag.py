while True:
    
    C= input("Drag Coeffecient= ")
    v= input("Velocity (m/s)= ")
    A= input("Frontal Area (m^2)= ")
    p= 1.225
    print("Force of drag= "+str(-0.5*C*A*p*(v*v))+str(" N"))
    print("________________")

