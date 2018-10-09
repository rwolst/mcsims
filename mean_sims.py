import sympy as sy

# Calculate the number of simulations (N) necessary for a certain confidence interval of E[P] (see Latex for more details)
sy.init_printing()
alpha, beta, gamma, n, N, t = sy.symbols('alpha, beta, gamma, n, N, t')

subs_values = {alpha: 50, beta: 50, n: 1000, gamma: 0.005}

## Define the moment generating function (Generalized Hypergeometric function)
MGF = sy.simplify(sy.hyper([-n, alpha], [alpha + beta], (1 - sy.exp(t))))

## Define function for getting moments (differentiating k times and substituting t=0)
def moment(k):
    return sy.diff(MGF, t, k).subs(t,0)

## Use 1.96 as the inverse normal of 0.975 but with numpy we can make epsilon another parameter
expr = (gamma**2 * n**2 * N)/(moment(2) - moment(1)**2) - 1.96**2

print('N: ')
print(sy.solve(expr.subs(subs_values), N))

mean = alpha/(alpha + beta)
true_mean = mean.subs(subs_values).evalf()
print('\nTrue mean:')
print(true_mean)

print('\nMean 95% bounds:')
print((true_mean - subs_values[gamma], true_mean + subs_values[gamma]))
