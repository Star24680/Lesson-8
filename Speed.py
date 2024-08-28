X=int(input("ENTER SPEEAD OF CYCLIST 1"))
Y=int(input("ENTER SPEEAD OF CYCLIST 2"))
Z=int(input("ENTER SPEEAD OF CYCLIST 3"))
A=(X+Y+Z)/3
print("Average is",A)
if A>X and A>Y and A>Z:
    print("%d is higher than %d,%d,%d" %(A,X,Y,Z))
elif A>X and A>Y:
    print("%d is higher than %d,%d" %(A,X,Y))
elif A>X and A>Z:
    print("%d is higher than %d,%d" %(A,X,Z))
elif A>Z and A>Y:
    print("%d is higher than %d,%d" %(A,Z,Y))
elif A>X:
    print("%d is higher than %d" %(A,X))
elif A>Y:
    print("%d is higher than %d" %(A,Y))
elif A>Z:
    print("%d is higher than %d" %(A,Z))
else:
    print("INVALID INPUT")