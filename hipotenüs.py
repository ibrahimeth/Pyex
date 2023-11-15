import math
while True:
    print("".center(100,"*"))
    a  = float(input("a kenarı :"))
    b = float(input("b kenarı :"))

    hipotenüsiçi = a**2 +b**2 
    hipotenüs = math.sqrt(hipotenüsiçi)

    print(f"Hiotenüs değeriniz : {hipotenüs} ")
