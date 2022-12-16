x=int(input("четверть="))

if x<=4 and x>0:
    if x ==1:
        print("x>0 and y>0")
    if x ==2:
        print("x<0 and y>0")
    if x ==3:
        print ("x<0 and y<0")
    if x ==4:
        print ("x>0 and y<0")
else:
    print ("incorrect input")