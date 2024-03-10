# import kniznice math ktoru pouzijeme
from math import sqrt

# interaktivne nacitanie konstant a,b,c pricom a> ako 0
print("Zadajte koeficienty a,b,c ako cele cisla oddelené čiarkami pre rovnicu v tvare ax^2 + bx+ c: ")

a,b,c = [float(coeficient) for coeficient in input().split(",")]

# vypocet diskriminantu D
d = pow(b, 2) - (4*a*c)

# vypocet korenov x1 a x2   
x1=(-b + sqrt(d))/(2*a)
x2=(-b - sqrt(d))/(2*a)

# zobrazenie vysledkov korenov x1 a x2
print("Riesenie x1 je {} a x2 je {}".format((x1),(x2)))

'''
Ako a zadajte 1
ako b zadajte 5
a ako c zadajte 6
'''