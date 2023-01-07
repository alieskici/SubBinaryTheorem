# https://github.com/alieskici/SubBinaryTheorem

# Length of main binary string
n = 10

# Sub binary string start and end index
i1 = 4
i2 = 9

# ------------------------>

z = ""
a = []

#create zeros
for i in range(n):
    z += "0"

b = ""
for i in range(2**n):
    b = bin(i)[2:]
    a.append(z[0:n-len(b)] + b)

c=[]
for i in range(2**n):
    c.append(a[i][i1:i2])

z = z[0:i2-i1]

for i in range(2**(i2-i1)):
    try:
        b = bin(i)[2:]
        b = z[0:len(z)-len(b)] + b
        print(c.index(b), b)
    except:
        print("error")
