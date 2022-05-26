n = int(input())
puncte = []
for i in range(n):
    x, y = [int(x) for x in input().split()]
    puncte.append((x,y))

def travers(x, y, z):
    a = (x[0] - z[0], x[1] - z[1])
    b = (y[0] - z[0], y[1] - z[1])
    return a[0]*b[1] - a[1]*b[0]

def intersect(x, y, z):
    if travers(x, z, y) != 0:
        return 0
    return (min(y[0], z[0]) <= x[0] and x[0] <= max(y[0],z[0])) and (min(y[1], z[1]) <= x[1] and x[1] <= max(y[1], z[1]))

def pozitie(punct):
    cnt = 0
    bnd = 0
    for i in range(n):
        if i == n-1:
            j = 0
        else:
            j = i+1
        if intersect(punct, puncte[i], puncte[j]):
            bnd = 1
        if puncte[i][0] <= punct[0] and punct[0] < puncte[j][0] and travers(puncte[i], puncte[j], punct) < 0:
            cnt += 1
        elif puncte[j][0] <= punct[0] and punct[0] < puncte[i][0] and travers(puncte[j], puncte[i], punct) < 0:
            cnt += 1
    if bnd:
        print("BOUNDARY")
    elif cnt % 2:
        print("INSIDE")
    else:
        print("OUTSIDE")

m = int(input())
for i in range(m):
    x, y = [int(x) for x in input().split()]
    punct = (x,y)
    pozitie(punct)