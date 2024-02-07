# Opening file
# with open(r'C:\Users\tomast\Documents\sss-trencin\license.txt','r') as f:
f = open(r'C:\Users\tomast\Documents\sss-trencin\sample.txt', 'r')

# reading everything in file
#r = f.read() # ako string
r = f.readlines()  #ako zoznam stringov po riadkoch

# reading at particular index
#r = f.readlines(17) # vrati pocet bytov z riadku

# print
print(r)
print(f.readlines())

