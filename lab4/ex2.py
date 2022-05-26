"""
min x1 + x2 + x3 + x4 + x5
x1 + x2 + x4 >= 1
x1 + x3 + x5 >= 1
x2 + x4 + x5 >= 1
0 <= x1 <= 1
0 <= x2 <= 1
0 <= x3 <= 1
0 <= x4 <= 1
0 <= x5 <= 1

we transform the three equations by multiplying them with -1
# because constraints need to be with <=
-x1 - x2 - x4 <= -1
-x1 - x3 - x5 <= -1
-x2 - x4 - x5 <= -1
"""

from scipy.optimize import linprog
obj = [1, 1, 1, 1, 1]

lhs_ineq = [[-1, -1, 0, -1, 0],
            [-1, 0, -1, 0, -1],
            [0, -1, 0, -1, -1]]

rhs_ineq = [-1, -1, -1]

bnd = [(0, 1),
       (0, 1),
       (0, 1),
       (0, 1),
       (0, 1)]

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,
              method="revised simplex")

print('\n'+opt.message+'\n')
if opt.success:
    print("X = "+str(opt.x))
    for i in range(len(opt.x)):
        if opt.x[i] >= 1/3:
            value = True
        else:
            value = False
        print("x{} = {}".format(i+1, value))