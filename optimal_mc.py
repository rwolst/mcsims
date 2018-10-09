import sympy as sy

# First get the symbolic expression for the asymptotic variance of our mean and variance
# estimators for p.

## Set symbols and pretty printing
n, alpha, beta, t, N = sy.symbols('n, alpha, beta, t, N')
sy.init_printing()

## Define the moment generating function (Generalized Hypergeometric function)
MGF = sy.simplify(sy.hyper([-n, alpha], [alpha + beta], (1 - sy.exp(t))))

## Define function for getting moments (differentiating k times and substituting t=0)
def moment(k):
    return sy.diff(MGF, t, k).subs(t,0)

## Set asymptotic variance of mean and variance
mean_asp_var = (moment(2) - moment(1)**2)/(N * n**2)
var_asp_var  = (moment(4) - moment(2)**2)/(N * n**4)

# Now set values that we require the mean and variance estimates to be within with prob ~95% i.e. 2sd values
## We want our 2*sd to be less than the *_gam values 
mean_gam = 0.0005
var_gam  = 0.0005

# Finally set the function to minimise (this relates to time taken for the whole MC run)
delta = 1  # This corresponds to the time required to set up a simulation for given hidden stats
time = N*(n + delta)

# Now set the alpha and beta parameters and perform the constrained optimisation
true_alpha = 0.5
true_beta = 0.5

constraint1 = (mean_gam/2)**2 - mean_asp_var.subs([(alpha, true_alpha), (beta, true_beta)])
constraint2 = (var_gam/2)**2 - var_asp_var.subs([(alpha, true_alpha), (beta, true_beta)])


sy.pprint(sy.simplify(constraint1))
sy.pprint(sy.simplify(constraint2))
sy.pprint(time)


# Lets solve constraints for N for different values of n
n_values = [1, 10, 100, 1000, 10000]
for n_value in n_values:
    print('n: {}'.format(n_value))
    print('constraint1 -> N: {}'.format(sy.solve(constraint1.subs(n, n_value))))
    print('constraint2 -> N: {}'.format(sy.solve(constraint2.subs(n, n_value))))
