import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
from scipy import optimize
 from scipy.optimize import Bounds

def obj_func(x):
    x1 = x[0]
    x2 = x[1]
    return x1**2 + x1*x2

def equality_constraint(x):
    x1 = x[0]
    x2 = x[1]
    # x1^3 + x1x2 = 100
    return x1 ** 3 + x1*x2 -100

def inequeality_constraint(x):
    x1 = x[0]
    x2 = x[0]
    # x1^3 + x1x2 >= 50
    return x1**3 + x1*x2 - 50

bounds_x1 = (-100,100)
bounds_x2 = (-100,100)
bounds = [bounds_x1, bounds_x2]
constraint1 = {'type':'eq','fun':equality_constraint}
constraint2 = {'type':'ineq','fun':inequeality_constraint}
constraint = [constraint1, constraint2]

x0 = [1,1]
result = minimize(obj_func, x0, method='trust-constr', bounds= bounds, constraints= constraint)
print(result)