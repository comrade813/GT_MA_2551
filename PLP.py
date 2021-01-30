from sympy import *
from sympy.vector import *
from IPython.display import display

C = CoordSys3D("C")

def get_point(indent):
    print(indent + "Point:\n" + indent + "\t(x,y,z): ", end="")
    tmp = input().strip(" ()").split(",")
    return Point3D(sympify(tmp[0]), sympify(tmp[1]), sympify(tmp[2]))

def get_vector(indent):
    print(indent + "Vector:\n" + indent + "\t(i,j,k): ", end="")
    tmp = input().strip(" ()").split(",")
    v = sympify(tmp[0])*C.i + sympify(tmp[1])*C.j + sympify(tmp[2])*C.k 
    return v

def vector_to_line(v, wrt=Point3D(0,0,0)):
    P = C.origin.locate_new('P',v)
    p = Point3D(P.express_coordinates(C))
    return Line(wrt,p)

def get_line(indent):
    print(indent + "Line:\n", end="")
    p1 = get_point(indent + "\t")
    p2 = get_point(indent + "\t")
    return Line(p1, p2)

def get_plane(indent):
    print(indent + "Plane:\n", end="")
    p = get_point(indent + "\t")
    v = get_vector(indent + "\t")
    return Plane(p, tuple(v.components.values()))

def get_object(arg):
    if arg == "plane":
        return get_plane("\t")
    elif arg == "line":
        return get_line("\t")
    elif arg == "point":
        return get_point("\t")

def handle_PLP(args):
    if args[0] == "cross":
        v1 = get_vector("\t")
        v2 = get_vector("\t")
        display(v1.cross(v2))
        return True
    elif args[0] == "dot":
        v1 = get_vector("\t")
        v2 = get_vector("\t")
        display(v1.dot(v2))
        return True
    elif args[0] == "magnitude_vector":
        v = get_vector("\t")
        display(v.magnitude())
        return True
    elif args[0] == "normalize":
        v = get_vector("\t")
        display(v.normalize())
        return True
    elif args[0] == "projection":
        if args[1] == "vector":
            u = get_vector("\t")
            v = get_vector("\t")
            display(v.projection(u))
        elif args[1] == "line":
            l1 = get_line("\t")
            l2 = get_line("\t")
            display(l2.projection(l1))
    elif args[0] == "angle":
        o1 = get_object(args[1])
        o2 = get_object(args[2])
        if args[2] == "plane":
            display(o2.angle_between(o1))
        else:
            display(o1.angle_between(o2))
        return True
    elif args[0] == "distance":
        o1 = get_object(args[1])
        o2 = get_object(args[2])
        if args[2] == "plane":
            display(o2.distance(o1))
        else:
            display(o1.distance(o2))
        return True
    elif args[0] == "intersect":
        o1 = get_object(args[1])
        o2 = get_object(args[2])
        if args[2] == "plane":
            display(o2.intersection(o1))
        else:
            display(o1.intersection(o2))
        return True