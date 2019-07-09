from itertools import combinations
nu ,qx = input().split()
qx = int(qx)
num = []
com = combinations(nu,len(nu)-qx)
for i in com:
    num.append("".join(i))
print(min(num))
