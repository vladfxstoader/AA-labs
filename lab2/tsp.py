# 1 - TSP
# 1.1
def read_data(filename):
    f = open(filename)
    cities = []
    for linie in f:
        x,y = [float(x) for x in linie.split()]
        cities.append((x,y))
    return cities

cities = read_data("tsp.in")
n = len(cities)

# 1.2
from math import sqrt
def distance(x,y):
    x1 = x[0]
    y1 = x[1]
    x2 = y[0]
    y2 = y[1]
    distance = sqrt((x2-x1)**2+(y2-y1)**2)
    return distance

# 1.3
def graph(cities):
    n = len(cities)
    matr = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                matr[i][j] = distance(cities[i], cities[j])
    return matr

matr = graph(cities)
# for i in range(n):
#     for j in range(n):
#         print(matr[i][j],end=" ")
#     print()

# 1.4
costs = []
def tsp(matr, viz, curr, n, cnt, cost,):
    if cnt == n and matr[curr][0]:
        costs.append(cost + matr[curr][0])
        return
    for i in range(n):
        if viz[i] == False and matr[curr][i]:
            viz[i] = True
            tsp(matr, viz, i, n, cnt + 1, cost + matr[curr][i])
            viz[i] = False

viz = [False for i in range(n)]
viz[0] = True
tsp(matr, viz, 0, n, 1, 0)
print("minimum cost is: "+str(min(costs)))

# 1.5
def tsp_approximate(matr, viz, curr, n, cnt, cost):
    mi = 999999
    poz = -1
    if cnt == n:
        for i in range(n):
            if viz[i] == False and matr[curr][i] and matr[curr][i] < mi:
                mi = matr[curr][i]
                poz = i
        viz[poz] = True
        cost = cost + matr[curr][poz]
        print("minimum cost using approximate algorithm is: "+str(cost))
        return
    for i in range(n):
        if viz[i] == False and matr[curr][i] and matr[curr][i] < mi:
            mi = matr[curr][i]
            poz = i
    viz[poz] = True
    #print(viz, poz, cost, matr[curr][poz])
    tsp_approximate(matr, viz, poz, n, cnt + 1, cost + matr[curr][poz])
viz = [False for i in range(n)]
viz[0] = True
tsp_approximate(matr, viz, 0, n, 1, 0)

# 1.6
parent = [i for i in range(n)]
INF = float('inf')

def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b

def kruskalMST(matr):
    mincost = 0

    for i in range(n):
        parent[i] = i

    edge_count = 0
    while edge_count < n - 1:
        min = INF
        a = -1
        b = -1
        for i in range(n):
            for j in range(n):
                if find(i) != find(j) and matr[i][j] < min and matr[i][j] != 0:
                    min = matr[i][j]
                    a = i
                    b = j
        union(a, b)
        # print(a, b)
        edge_count += 1
        mincost += min

    print("Minimum cost= {}".format(mincost))

kruskalMST(matr)


