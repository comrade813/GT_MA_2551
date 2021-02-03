# Introduction
- The code is meant to be run in Jupyter Notebook or something like it, so that results from each query can be displayed in latex
- This code is not meant to (but sometimes does) give you the correct or most optimal answer, it functions better as a way to check your work.
- Please note that the results given may not be the most simplified possible, but probably are equal to the correct answer.

# Installation
# Python3
Python is the language the code is in so obviously you need it to run.
Mac:
- brew install python3
if you don't have homebrew you should get it because its really helpful for a lot of installations

Windows:
- https://www.python.org/downloads/release/python-391/
- go there, scroll to the bottom, and download the right python package (the one that matches your OS)
- follow installation instructions

## SymPy
SymPy is the python library that does all the vector/line/plane and calculus stuff.
Mac and Windows:
- pip3 comes automatically with python3, and is used to install all sorts of fun stuff
- in terminal, type "pip3 install sympy"

## IPython
IPython allows your input/output to be printed in cool LaTeX.
Mac and Windows:
- in terminal, type "pip3 install ipython"

## Jupyter Notebook
This is the place which allows you to run the Python code interactively i.e. you get to see the cool LaTeX
Mac and Windows:
- in terminal, type "pip3 install notebook"

# Using The Program
## Setup
- make sure all the Python files (especially the main.ipynb file) is in the same folder
- navigate to that folder in the command line
- type "jupyter notebook"
- after the notebook opens in your browser, click on the "main.ipynb" file
- click on the first block (which should be the only block with code, if there are multiple blocks)
- click "run"
- enter the input in the little space box it gives you

## Commands
- Understand that very, very little error checking of input has been done, since error checking would make my program unbearably long. So it is up to you to type in the equations/points/vectors whatever correctly or else the program will crash
- if the program crashes no big deal just hit "run" again and enter it right
- if you can't figure out why something's not working, or if something isn't right, contact me through groupme or send me an email at kzheng74@gatech.edu
- some additional notes: for some reason sympy's simplify function doesn't recognize log(e) as 1, so you'll have to simplify that yourself. Also, at times, simplify() won't cancel equivalent expressions in the numerator and denominator if they're under a square root -- you'll see what I mean as you do more problems. Just factor it yourself, its usually not that difficult.

#### Basic Objects
##### Point
- when asked for a vector the input should be in the form of: (x,y,z)
- no spaces
##### Vector
- when asked for a vector the input should be in the form of: (i,j,k)
- no spaces
- each i,j,k can be an equation
##### Line
- a line is defined by two points
- if the line you are trying to input is in the form of a point and a vector, take the extra 3 seconds to find a second point
##### Plane
 - a plane is defined by a point and its normal vector
##### Equation
- you mostly know how to type an equation, i.e. "\*" to multiply, "/" to divide, "+" to add, "-" to subtract, "^" or "\*\*" for exponents, etc.
- warning: if you have an equation like "24x", you must write "24\*x" or else it won't work
- use parentheses literally everywhere so the equation you typed doesn't get messed up by order of operations
- the program will print out a LaTeX version of the equation you typed after you enter it so you can check

#### Chapter 12
##### cross
- line contains no other arguments
- gets the cross product of two vectors
##### dot
- line contains no other arguments
- gets the dot product of two vectors
##### magnitude_vector
- line contains no other arguments
- gets the magnitude of a vector
##### normalize
- line contains no other arguments
- normalizes a vector
##### projection
- line contains no other arguments
- projects the first vector onto the second vector (make sure you don't get them mixed up)
##### angle
- line contains 2 other arguments, with each being either "line", "vector", or "plane" depending on what you want to find the angle between; 
- i.e. type "angle line plane" as input to get angle between a line and a plane
- you will be asked for further input depending on your arguments
##### distance
- line contains 2 other arguments, with each being either "point", "line", or "plane" depending on what you want to find the angle between; 
- i.e. type "angle line plane" as input to get distance between a line and a plane
- you will be asked for further input depending on your arguments
##### intersect
- line contains 2 other arguments, with each being either "point", "line", or "plane" depending on what you want to find the angle between; 
- i.e. type "intersect plane plane" as input to get the intersection between two planes
- you will be asked for further input depending on your arguments

#### Chapter 13
- sidenote: when I say "function", I mean either function or parametric equation; but if an argument is specified to be a parametric equation, you must use a parametric equation
##### function
- line contains 1 other argument: the name of the function you want defined for later use
- i.e. "function f(x)"
- you will then input the equation of the function, then the symbol used in the equation for the variable (useful later for taking derivatives with respect to that variable)
- note: only x, y, z, and t are supported as symbols
##### parametric
- line contains 1 other argument: the name of the function you want defined for later use
- i.e. "parametric r(t)"
- you will then input three separate equations for i, j, and k respectively, then the symbol used as the main variable
##### last_eq
- line contains 1 other argument: the name of the function you want defined for later use
- "last_eq f'(x)"
- copies the last function/equation found in calculation. useful for example when you get the derivative of a function then you want to do stuff with that derivative
##### diff
- line contains 1 other argument: the name of the function you want to use (must be pre-defined)
- "diff f(x)"
- gets derivative of the function name passed in
##### ddiff
- line contains 1 other argument: the name of the function you want to use (must be pre-defined)
- "ddiff f(x)"
- gets double derivative of the function name passed in
##### eval
- line contains 2 other argument: the name of the function you want to use (must be pre-defined), and the value to replace the main variable
- "eval f(x) 2" is effectively the same as "f(2)" normally
- evaluates a function at a specific point/time/value
##### get_0
- line contains 1 other argument: the name of the function you want to use (must be pre-defined)
- "get_0 f(x)"
- returns the points at which f(x) = 0
- useful in tandem with other operations. for example, if you want to find min/max of a function, run the following commands: "diff f(x)", "last_eq f'(x)", "get_0 f'(x)", then copy paste one of the values to "eval f(x) *value*"
##### magnitude_parametric
- line contains 1 other argument: the name of the parametric equation you want to use (must be pre-defined)
- "magnitude_parametric r(t)"
- displays the function which is the magnitude of the parametric function
##### integrate
- if the line contains 1 other argument: the name of the function you want to use (must be pre-defined)
    - "integrate f(x)"
    - displays the integral of f(x)
- line contains 2 other arguments: the name of the function you want to use (must be pre-defined), and two values
    - "integrate f(x) 0 pi/2"
    - displays the integral of f(x) with those two values as lower and upper bound, respectively
##### arclength
- if the line contains 1 other argument: the name of the parametric equation you want to use (must be pre-defined)
    - "arclength r(t)"
    - displays the arclength as a parametric of f(x)'s symbol
- if the line contains 2 other arguments: the name of the parametric equations you want to use (must be pre-defined), and two other values
    - "arclength r(t) 0 pi/2"
    - displays the arclength from the first to the second value
##### speed
- line contains 1 other argument: the name of the function you want to use (must be pre-defined)
- "speed f(x)"
- displays the speed of a parametric equation
##### unit_tangent
- line contains 1 other argument: the name of the parametric equation you want to use (must be pre-defined)
- "unit_tangent r(t)"
- displays the unit tangent vector T
##### curvature_parametric
- line contains 1 other argument: the name of the parametric equation you want to use (must be pre-defined)
- "curvature_parametric r(t)"
- displays the curvature of r(t) as a function
##### curvature_function
- line contains 1 other argument: the name of the function you want to use (must be pre-defined)
- "curvature_function f(x)"
- displays the curvature of f(x) as a function
##### principal_unit_normal
- line contains 1 other argument: the name of the parametric equation you want to use (must be pre-defined)
- "principal_unit_normal r(t)"
- displays the principal unit normal vector N
##### acceleration_tangential
- line contains 1 other argument: the name of the parametric equation you want to use (must be pre-defined)
- "acceleration_tangential r(t)"
- displays the tangential acceleration of r(t)
##### acceleraiton_normal
- line contains 1 other argument: the name of the parametric equation you want to use (must be pre-defined)
- "acceleration_normal r(t)"
- displays the normal acceleration of r(t)
##### binormal
- line contains 1 other argument: the name of the parametric equation you want to use (must be pre-defined)
- "binormal r(t)"
- displays the binormal vector of r(t) (equals T cross N)
##### torsion
- line contains 1 other argument: the name of the parametric equation you want to use (must be pre-defined)
- "torsion r(t)"
- displays the torsion of r(t)
