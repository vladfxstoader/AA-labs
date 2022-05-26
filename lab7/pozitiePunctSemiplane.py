def intersectie(halfplanes, point):
    xmax, ymax = 9999999999, 9999999999
    xmin, ymin = -9999999999, -9999999999

    for halfplane in halfplanes:
        if halfplane[0] == 0:  # vertical
            if (halfplane[2]+ halfplane[1] * point[1] ) >= 0:
                continue
        else:  # horizontal
            if (halfplane[2] + halfplane[0] * point[0] ) >= 0:
                continue

        if halfplane[0] == 0:  # vertical
            if -1 * halfplane[2] / halfplane[1] < point[1]:
                ymin = max(ymin, -1 * halfplane[2] / halfplane[1])
            else:
                ymax = min(ymax, -1 * halfplane[2] / halfplane[1])
        else:  # horizontal
            if -1 * halfplane[2] / halfplane[0] < point[0]:
                xmin = max(xmin, -1 * halfplane[2] / halfplane[0])
            else:
                xmax = min(xmax, -1 * halfplane[2] / halfplane[0])

    if xmax == 9999999999 or ymax == 9999999999 or xmin == -9999999999 or ymin == -9999999999:
        return 0
    return (xmax - xmin) * (ymax - ymin) # surface

halfplanes = []
n = int(input())
for i in range(n):
    line = [int(x) for x in input().split()]
    halfplane = (line[0], line[1], line[2])
    halfplanes.append(halfplane)

m = int(input())
for i in range(m):
    line = [float(x) for x in input().split()]
    point = (line[0], line[1])
    output = intersectie(halfplanes, point)
    if output == 0:
        print("NO")
    else:
        print("YES")
        print(output)