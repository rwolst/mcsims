import sympy

# Set symbols and pretty printing
n, alpha, beta, t = sympy.symbols('n, alpha, beta, t')
sympy.init_printing()

# Define expression as Generalised Hypergeometric function (this is MGF of Beta-Binomial)
MGF = sympy.simplify(sympy.hyper([-n, alpha], [alpha+beta], (1-sympy.exp(t))))

# Get the moments by differentiating and substituting t=0
def moment(k):
    return sympy.diff(MGF, t, k).subs(t,0)

sympy.pprint(sympy.simplify(moment(1)))

sympy.pprint(sympy.simplify(moment(4) - moment(2)**2))

# The best we can do as n->oo
sympy.pprint(sympy.limit(sympy.simplify(moment(4)/n**4), n, sympy.oo))

# Example:
# The mean 
expr = moment(2)/n**2
sympy.pprint(sympy.simplify(expr.subs([(alpha, 0.5), (beta, 0.5)])))
