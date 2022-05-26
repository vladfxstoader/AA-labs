"""
maximize z = 180x + 200y
5x + 4y <= 80
10x + 20y <= 200
x >= 0
y >= 0
"""

# instead of maximizing x = 180x + 200y, we minimize its negative
# -z = -180x - 200y (linprog solves only minimization problems)

from scipy.optimize import linprog

obj = [-180, -200]      # coefficients for x and y

lhs_ineq = [[5, 4],     # coefficients of the left side of
            [10, 20]]   # the two inequalities

rhs_ineq = [80, 200]    # right side of the two inequalities

bnd = [(0, float("inf")),
       (0, float("inf"))]   # bounds of x and y

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,
              method="revised simplex")

print('\n'+opt.message+'\n')
if opt.success:
    print("Optimal function value = "+str(-opt.fun))
    print("X = "+str(opt.x))