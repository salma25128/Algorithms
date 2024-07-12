# algorithms analysis from scratch

#  CALCULATE PARALLELO GRAM AREA
def Parallelo():
    b = int(input("enter base value: "))
    h = int(input("enter height value: "))
    a = b*h
    return a
print(Parallelo())


#  CALCULATE trapezoid GRAM AREA

def Trapezoid():
    at= int(input("enter base value: "))
    bt = int(input("enter height value: "))
    ht = int(input("enter height value: "))
    area = 0.5*(at+bt)*ht
    return area

print(Trapezoid())