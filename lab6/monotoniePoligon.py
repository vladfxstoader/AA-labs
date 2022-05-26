n = int(input())
puncte = []
xmin = 10000000000
xmax = -10000000000
ymin = 10000000000
ymax = -10000000000
punct_xmin = None
punct_xmax = None
punct_ymin = None
punct_ymax = None
pos_xmin = None
pos_xmax = None
pos_ymin = None
pos_ymax = None
for i in range(n):
    x, y = [int(x) for x in input().split()]
    if y > ymax:
        pos_ymax = i
        ymax = y
        punct_ymax = (x,y)
    if y < ymin:
        pos_ymin = i
        ymin = y
        punct_ymin = (x,y)
    if x > xmax:
        pos_xmax = i
        xmax = x
        punct_xmax = (x,y)
    if x < xmin:
        pos_xmin = i
        xmin = x
        punct_xmin = (x,y)
    puncte.append((x,y))

i = pos_xmin
ok = 0
while i != pos_xmax%n - 1:
    if puncte[i][0] > puncte[((i+1)%n)][0]:
        ok = 1
        break
    i = (i+1) % n
if puncte[i][0] > puncte[pos_xmax][0]:
    ok = 1
i = (pos_xmax + 1) % n
while i != pos_xmin%n + 1:
    if puncte[i-1][0] < puncte[i][0]:
        ok = 1
        break
    i = (i+1) % n
if ok == 0:
    print("YES")
else:
    print("NO")
i = pos_ymin
ok = 0
while i != pos_ymax:
    if puncte[i][1] > puncte[((i+1)%n)][1]:
        ok = 1
        break
    i = (i+1) % n
i = (pos_ymax + 1) % n
while i != pos_ymin + 1:
    if puncte[i-1][1] < puncte[i][1]:
        ok = 1
        break
    i = (i+1) % n
if ok == 0:
    print("YES")
else:
    print("NO")