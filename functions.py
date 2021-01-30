from sympy import *
from sympy.vector import *
from IPython.display import display
from sympy.solvers import solve

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

C = CoordSys3D("C")
init_printing(use_latex=True)
    
func = dict()
last_eq = [None,None]

def get_function(indent, name):
    try:
        print(indent + name + " = ", end="")
        f = sympify(input())
        return f
    except SympifyError:
        print("Equation invalid")
        return None

def get_symbol(indent):
    try:
        print(indent + "symbol: ", end="")
        sym = sympify(input())
        return sym
    except SympifyError:
        print("Symbol invalid")
        return None

def add_function(indent, name):
    f = get_function(indent, name)
    if f == None:
        print("Could not add function.")
        return False
    sym = get_symbol(indent)
    if f == None:
        print("Could not add function.")
        return False
    func[name] = (f, sym)
    display(f)

def add_parametric(indent, name):
    print(indent + name + " =")
    f_i = get_function(indent+"\t", "i")
    if f_i == None:
        print("Could not add curve.")
        return False
    f_j = get_function(indent+"\t", "j")
    if f_j == None:
        print("Could not add curve.")
        return False
    f_k = get_function(indent+"\t", "k")
    if f_k == None:
        print("Could not add curve.")
        return False
    sym = get_symbol(indent)
    if sym == None:
        print("Could not add function.")
        return False
    v = f_i*C.i + f_j*C.j + f_k*C.k
    func[name] = (v, sym)
    display(func[name])

def show(ans):
    display(ans)
    print("Alternate (but equal) representation:")
    display(simplify(ans))

def handle_functions(args):
    global func, last_eq
    if args[0] == "function":
        add_function("\t", args[1])
    elif args[0] == "parametric":
        add_parametric("\t", args[1])
    elif args[0] == "last_eq":
        if last_eq[0] == None:
            print("No previous equation. Cannot add function.")
            return False
        func[args[1]] = (last_eq[0],last_eq[1])
    elif args[0] == "diff":
        last_eq[0] = diff(func[args[1]][0], func[args[1]][1])
        last_eq[1] = func[args[1]][1]
        show(last_eq[0])
    elif args[0] == "ddiff":
        last_eq[0] = diff(func[args[1]][0], func[args[1]][1], 2)
        last_eq[1] = func[args[1]][1]
        show(last_eq[0])
    elif args[0] == "get_0":
        display(solve(func[args[1]][0], func[args[1]][1]))
    elif args[0] == "magnitude_parametric":
        last_eq[0] = func[args[1]][0].magnitude()
        last_eq[1] = func[args[1]][1]
        show(last_eq[0])
    elif args[0] == "integrate":
        if len(args) == 2:
            last_eq[0] = integrate(func[args[1]][0], func[args[1]][1])
            last_eq[1] = func[args[1]][1]
            show(last_eq[0])
        elif len(args) == 4:
            ans = integrate(func[args[1]][0], (func[args[1]][1], sympify(args[2]), sympify(args[3])))
            show(ans)
    elif args[0] == "eval":
        if len(args) != 3:
            print("Invalid number of arguments")
            return False
        try:
            print(func[args[1]][0].subs(func[args[1]][1], float(args[2])))
        except ValueError:
            print("Third argument has to be a float")
    elif args[0] == "arclength":
        v = diff(func[args[1]][0], func[args[1]][1])
        if len(args) == 2:
            last_eq[0] = integrate(v.magnitude(), func[args[1]][1])
            last_eq[1] = func[args[1]][1]
            show(last_eq[0])
        else:
            exp = integrate(v.magnitude(), (func[args[1]][1],sympify(args[2]),sympify(args[3])))
            show(exp)
    elif args[0] == "speed":
        v = diff(func[args[1]][0], func[args[1]][1])
        last_eq[0] = v.magnitude()
        last_eq[1] = func[args[1]][1]
        show(last_eq[0])
    elif args[0] == "unit_tangent":
        v = diff(func[args[1]][0], func[args[1]][1])
        last_eq[0] = v.normalize()
        last_eq[1] = func[args[1]][1]
        show(last_eq[0])
    elif args[0] == "curvature_parametric":
        v = diff(func[args[1]][0], func[args[1]][1])
        T = v.normalize()
        last_eq[0] = diff(T,func[args[1]][1]).magnitude()/v.magnitude()
        last_eq[1] = func[args[1]][1]
        show(last_eq[0])
    elif args[0] == "curvature_function":
        f__ = Abs(diff(func[args[1]][0], func[args[1]][1],2))
        f_ = diff(func[args[1]][0], func[args[1]][1])
        last_eq[0] = f__/(1 + (f_)**2)**(3/2)
        last_eq[1] = func[args[1]][1]
        show(last_eq[0])
    elif args[0] == "principal_unit_normal":
        T = diff(func[args[1]][0], func[args[1]][1]).normalize()
        last_eq[0] = diff(T,func[args[1]][1]).normalize()
        last_eq[1] = func[args[1]][1]
        show(last_eq[0])
    elif args[0] == "acceleration_tangential":
        v = diff(func[args[1]][0], func[args[1]][1])
        last_eq[0] = diff(v.magnitude(),func[args[1]][1])
        last_eq[1] = func[args[1]][1]
        show(last_eq[0])
    elif args[0] == "acceleration_normal":
        v = diff(func[args[1]][0], func[args[1]][1])
        T = v.normalize()
        k = diff(T,func[args[1]][1]).magnitude()/v.magnitude()
        last_eq[0] = k*(v.magnitude()**2)
        last_eq[1] = func[args[1]][1]
        show(last_eq[0])
    elif args[0] == "torsion":
        v = diff(func[args[1]][0], func[args[1]][1])
        T = v.normalize()
        N = diff(T,func[args[1]][1]).normalize()
        B = T.cross(N)
        last_eq[0] = -1*(diff(B,func[args[1]][1])/v.magnitude()).dot(N)
        last_eq[1] = func[args[1]][1]
        show(last_eq[0])