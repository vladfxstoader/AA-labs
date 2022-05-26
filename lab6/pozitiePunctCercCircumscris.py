def determinant(x, y, z):
    sum = x[0]*y[1]*(z[0]**2 + z[1]**2) + x[1] * (y[0]**2 + y[1]**2) * z[0] + y[0] * z[1] * (x[0]**2 + x[1]**2)
    sum = sum - (x[0] ** 2 + x[1] ** 2) * y[1] * z[0] - z[1] * (y[0]**2 + y[1]**2) * x[0] - x[1] * y[0] * (z[0]**2 + z[1]**2)
    return sum

def calcul(a, b, c, p):
    det =  - determinant(b, c, p) + determinant(a, c, p) - determinant(a, b, p) + determinant(a, b, c)
    return  det

xa, ya = [int(x) for x in input().split()]
a = (xa, ya)
xb, yb = [int(x) for x in input().split()]
b = (xb, yb)
xc, yc = [int(x) for x in input().split()]
c = (xc, yc)
m = int(input())
for i in range(m):
    xp, yp = [int(x) for x in input().split()]
    p = (xp, yp)
    if calcul(a, b, c, p) > 0:
        print("INSIDE")
    elif calcul(a, b, c, p) == 0:
        print("BOUNDARY")
    else:
        print("OUTSIDE")