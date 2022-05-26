def testOrientare(P, Q, R):
    p1 = P[0]
    p2 = P[1]
    q1 = Q[0]
    q2 = Q[1]
    r1 = R[0]
    r2 = R[1]
    det = q1*r2 + r1*p2 + p1*q2 - q1*p2 - r1*q2 - p1*r2
    if det == 0:
        print("TOUCH")
    elif det < 0:
        print("RIGHT")
    else:
        print("LEFT")

t = int(input())
for i in range(t):
    line = [int(x) for x in input().split()]
    P = (line[0], line[1])
    Q = (line[2], line[3])
    R = (line[4], line[5])
    testOrientare(P, Q, R)