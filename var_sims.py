import sympy as sy
import math

# Calculate the number of simulations (N) necessary for a certain confidence interval of var(P) (see Latex for more details)
sy.init_printing()
alpha, beta, gamma, n, N, t = sy.symbols('alpha, beta, gamma, n, N, t')

subs_values = {alpha: 50, beta: 50, n: 1000, gamma: 0.0005}

## Define the moment generating function (Generalized Hypergeometric function)
MGF = sy.simplify(sy.hyper([-n, alpha], [alpha + beta], (1 - sy.exp(t))))

## Define function for getting moments (differentiating k times and substituting t=0)
def moment(k):
    return sy.diff(MGF, t, k).subs(t,0)

## Use 1.96 as the inverse normal of 0.975 but with numpy we can make epsilon another parameter
expr = (gamma**2 * n**4 * N)/(moment(4) - 4*moment(3)*moment(1) + 8*moment(2)*moment(1)**2 - 4*moment(1)**4 - moment(2)**2) - 1.96**2

print('N: ')
print(sy.solve(expr.subs(subs_values), N))

var = alpha*beta/((alpha + beta)**2 * (alpha + beta + 1))
true_var = var.subs(subs_values).evalf()
print('\nTrue variance:')
print(true_var)

print('\nTrue standard deviation:')
print(math.sqrt(true_var))

print('\nVariance 95% bounds:')
print((true_var - subs_values[gamma], true_var + subs_values[gamma]))

print('\nStandard deviation 95% bounds:')
if true_var - subs_values[gamma] < 0:
    print((0, math.sqrt(true_var + subs_values[gamma])))
else: 
    print((math.sqrt(true_var - subs_values[gamma]), math.sqrt(true_var + subs_values[gamma])))
