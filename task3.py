# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

x=int(input("x="))
y=int(input("y="))
if x!=0 and y!=0:
    if x > 0 and y > 0:
        print("first")
    if x > 0 and y < 0:
        print("fourth")
    if x < 0 and y > 0:
        print ("second")
    if x < 0 and y < 0:
        print ("third")
else:
    print ("incorrect input")