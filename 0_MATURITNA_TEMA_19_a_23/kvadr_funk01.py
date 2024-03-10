# pouzitie matematickej kniznice cmath pre komplexne cisla
import cmath

# interaktivne nacitanie konstant a,b,c pricom a> ako 0
a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
c=float(input("enter value of c:"))

# vypocet diskriminantu D
d=(b**2)-(4*a*c)   

# vypocet korenov x1 a x2   
x1=(-b+cmath.sqrt(d))/(2*a)
x2=(-b-cmath.sqrt(d))/(2*a)

# zobrazenie vysledkov v komplexnom tvare
print("Koren x1 je {} a koren x2 je {}".format((x1),(x2)))

""" 
zadajte hodnotu a:1
zadajte hodnotu b:5
zadajte hodnotu c:6

riešenia sú (-2+0j) a (-3+0j)
"""