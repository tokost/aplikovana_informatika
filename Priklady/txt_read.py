# Open a file
# fo = open("riadky.txt", "rw+") # môže byť použitý iba jeden parameter
fo = open("riadky.txt", "r")
print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readline(5)
print("Read Line Nr.1: %s" % (line))

line = fo.readlines(18)
print ("Read Line Nr.2: %s" % (line))

line = fo.readlines()
print ("Read Line Nr.3: %s" % (line))

# Close opend file
fo.close()

"""
Metóda súboru Python readlines() číta do EOF (End Of File) pomocou 
readline() a vracia zoznam obsahujúci riadky. Ak je prítomný 
voliteľný argument sizehint , namiesto čítania do EOF sa čítajú 
celé riadky s celkovou veľkosťou bajtov sizehint (pravdepodobne po 
zaokrúhlení nahor na veľkosť vnútornej vyrovnávacej pamäte).

Syntax

fileObject.readline( sizehint ) # vráti počet bajtov 1 riadku

fileObject.readlines( sizehint ) # vráti vštky riadky az po počet bytov

sizehint − počet bajtov

Návratová hodnota
Táto metóda vráti zoznam (list) obsahujúci riadky.

"""
