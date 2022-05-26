def intersection(halfplanes):
    xmax, ymax = 9999999999, 9999999999 # we take a first halfplane that helps us get the intersection
    xmin, ymin = -9999999999, -9999999999

    for halfplane in halfplanes:    # getting the "edge" of every halfplane
        left = -9999999999
        right = 9999999999
        
        if halfplane[0] == 0: # vertical
            if halfplane[1] < 0:
                left = -1 * halfplane[2] / halfplane[1]
            else:
                right = -1 * halfplane[2] / halfplane[1]

        else: # horizontal
            if halfplane[0] < 0:
                left = -1 * halfplane[2] / halfplane[0]
            else:
                right = -1 * halfplane[2] / halfplane[0]

        if halfplane[0] == 0: # vertical
            ymin = max(ymin, left)
            ymax = min(ymax, right)
        else: # horizontal
            xmin = max(xmin, left)
            xmax = min(xmax, right)

    if ymin > ymax or xmin > xmax:
        return 0 # VOID
    
    if (xmin != -9999999999 and xmax != 9999999999) and (ymin != -9999999999 and ymax != 9999999999):
        return 1 # BOUNDED
    
    return 2 # UNBOUNDED


halfplanes = []
n = int(input())
for i in range(n):
    line = [int(x) for x in input().split()]
    halfplane = (line[0], line[1], line[2])
    halfplanes.append(halfplane)

output = intersection(halfplanes)
if output == 0:
    print("VOID")
elif output == 1:
    print("BOUNDED")
else:
    print("UNBOUNDED")