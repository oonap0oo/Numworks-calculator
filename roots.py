# As described in NUMERICAL METHODS FOR ENGINEERS  8th Edition

from math import *

def incremental(f, interval, n_steps):
    """incremental search for sign c-changes
    f: function of one argument to search
    n_steps: number of points to evaluate f on"""
    xl, xu = interval
    x_old = xl
    y,s = eval_fun(f, x_old)
    if s==False:
        return []
    sign_old = copysign(1, y)
    intervals = []
    for step in range(n_steps):
        x = xl + (xu - xl) * step / (n_steps - 1)
        y,s = eval_fun(f, x)
        if s==False:
            return []
        sign = copysign(1, y)
        if sign != sign_old:
            intervals.append([x_old, x])
        x_old = x
        sign_old = sign
    return intervals

def modfalsepos(f, interval, imax, es):
    """Modified false position method
    f: function of one argument to find root of
    interval: iterable with lowel and upper guess (xl,xu)
    imax: max allowed number of iterations
    es: maximum relative error allowed in %
    """
    xl, xu = interval # lower and upper guesses
    iter_ = 0
    fl,s = eval_fun(f, xl)
    if s==False:
        return (None)*4
    fu,s = eval_fun(f, xu)
    if s==False:
        return (None)*4
    xr = xu
    iu = 0; il = 0
    while True:
        xr_old = xr # save previous root estimation
        xr = xu - fu * (xl - xu) / (fl - fu) # new estimate for root
        fr,s = eval_fun(f, xr) # function value at new root estimate
        if s==False:
            return (None)*3
        iter_ += 1
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100 # relative error estimate in %
        test = fl * fr
        if test < 0: # values of function at xr and xl have different signs
            xu = xr # root must be in lower half of interval
            fu,s = eval_fun(f, xu)
            if s==False:
                return (None)*3
            iu = 0 # start counting if lower half more then 2 times reduce function value lower limit fl
            il += 1
            if il >= 2:
                fl /= 2
        elif test > 0: # values of function at xr and xl have same signs
            xl = xr # root must be in upper half of interval
            fl,s = eval_fun(f, xl)
            if s==False:
                return (None)*3
            il = 0 # start counting if upper half more then 2 times reduce function value upper limit fu
            iu += 1
            if iu >=2:
                fu /= 2
        else:
            ea = 0 # fr must be zero, then xr is root
        if ea < es: # rel error small enough
            break
        elif iter_ >= imax: # max iter reached
            print("Maximum Iterations reached")
            return (None)*3
    return xr, iter_, ea


def eval_fun(fun, x):
    """Calculate function value for given x
    x: float value to evaluate function with"""
    global_dict = { "x": x, "__builtins__": {}}
    global_dict.update(math_fun_dict)
    try:
        f = eval(fun, global_dict)
    except NameError:
        print("ERROR: function contains unknown variables other then x")
        return None, False
    except ValueError:
        print("ERROR: function is not a valid real function over given interval")
        return None, False
    except SyntaxError:
        print("ERROR: invalid syntax detected in function")
        return None, False
    except ZeroDivisionError:
        print("ERROR: Division by zero")
        return None, False
    except TypeError:
        print("ERROR: Invalid expression for f(x)")
        return None, False
    return f, True


def input_value(prompt, default, value_type):
    """Get user input providing prompt and default choice
       prompt: text to display when asking for input
       default: returned result when user just presses return
       value_type: type user input is converted to, float or int"""
    valid = False
    while not valid:
        answer = input(prompt + "\nHit enter for " + str(default) + ": ")
        if answer == "":
            return default
        try:
            if value_type == int:
                value = int(answer)
            elif value_type == float:
                value = float(answer)
        except:
            valid = False
        else:
            valid = True
    return value
            

def get_input():
    """Get user input for function, bounds, max. interations and rel. error"""
    valid = False
    while not valid:
        print("Key words which can be used:")
        funcs=list(math_fun_dict.keys())
        for k in range(len(funcs)):
            print(funcs[k]+" ", end="")
            if (k+1)%6==0:
                print()
        fun = input("\nFunction to find roots of\nf(x) = ").lower()
        if fun != "":
            valid = True 
    xl = input_value("Lower boundary for x", -1.0, float)
    xu = input_value("Upper boundary for x", 1.0, float)
    if xl > xu:
        xl, xu = xu, xl
    return fun, xl, xu


def main_loop():
    terminate = False
    while not terminate:
        print("\nRoots of function:")
        print("------------------")
        fun, xl, xu = get_input() # get user input
        results = incremental(fun, (xl, xu), N) # search for zero crossings, results is list of lists [xl, xu]
        if len(results)>0:
            print("\nFound {0} roots:".format(len(results)))
            for xl, xu in results:
                root, steps, rel_error = modfalsepos(fun, (xl, xu), N, es)
                print("root x = {0}".format(root))
                res,s = eval_fun(fun, root)
                print("residual: {0:.2}".format(res))
        else:
            print("No roots found in given interval")
        answer = input("Another search? (y/n)").lower()
        if answer != "y":
            terminate = True


# functions which can be used in eval()
math_fun_dict = {   
  "pi": pi, "e": e, "sqrt": sqrt,
  "log": log, "exp": exp, "log10": log10,
  "sin": sin, "cos": cos, "tan": tan,
  "asin": asin, "acos": acos, "atan": atan,
  "atan2": atan2, "abs": abs}

# parameters
es = 0.01 # Maximum allowed percentage error
N = 300 # Maximum number of iterations

main_loop()        

