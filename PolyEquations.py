import math
import cmath
import numpy as np 

#Mapping labels to their digits and operations
dic={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'+',11:'-',12:'=',13:'x'}

#print equation 
def printEq(x):
    flag=0
    for i in range(len(x)):
        if flag==1:
            flag=0
            continue
        if i!=len(x)-1 and dic[x[i]]=='x'and x[i+1]!=10 and x[i+1]!=11 and x[i+1]!=12:
            print('x^'+str(dic[x[i+1]]), end=" ")
            flag=1
        else :
            print(dic[x[i]], end=" ")

# Find degree of polynomial
def highdegree(x):
    Max=1
    for i in range(len(x)):
        if i!=len(x)-1 and x[i]==13 and x[i+1]!=10 and x[i+1]!=11 and x[i+1]!=12:
            Max=max(Max,x[i+1])
    return Max     

# Helper function to return float value of f.
def findF(a, b, c):
    return ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0


# Helper function to return float value of g.
def findG(a, b, c, d):
    return (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a **2.0)) + (27.0 * d / a)) /27.0


# Helper function to return float value of h.
def findH(g, f):
    return ((g ** 2.0) / 4.0 + (f ** 3.0) / 27.0)

def cubic_solver(a, b, c, d):

    if (a == 0 and b == 0):                     # Case for handling Liner Equation
        return np.array([(-d * 1.0) / c])                 # Returning linear root as numpy array.

    elif (a == 0):                              # Case for handling Quadratic Equations

        D = c * c - 4.0 * b * d                       # Helper Temporary Variable
        if D >= 0:
            D = math.sqrt(D)
            x1 = (-c + D) / (2.0 * b)
            x2 = (-c - D) / (2.0 * b)
        else:
            D = math.sqrt(-D)
            x1 = (-c + D * 1j) / (2.0 * b)
            x2 = (-c - D * 1j) / (2.0 * b)
            
        return np.array([x1, x2])               # Returning Quadratic Roots as numpy array.

    f = findF(a, b, c)                          # Helper Temporary Variable
    g = findG(a, b, c, d)                       # Helper Temporary Variable
    h = findH(g, f)                             # Helper Temporary Variable

    if f == 0 and g == 0 and h == 0:            # All 3 Roots are Real and Equal
        if (d / a) >= 0:
            x = (d / (1.0 * a)) ** (1 / 3.0) * -1
        else:
            x = (-d / (1.0 * a)) ** (1 / 3.0)
        return np.array([x, x, x])              # Returning Equal Roots as numpy array.

    elif h <= 0:                                # All 3 roots are Real

        i = math.sqrt(((g ** 2.0) / 4.0) - h)   # Helper Temporary Variable
        j = i ** (1 / 3.0)                      # Helper Temporary Variable
        k = math.acos(-(g / (2 * i)))           # Helper Temporary Variable
        L = j * -1                              # Helper Temporary Variable
        M = math.cos(k / 3.0)                   # Helper Temporary Variable
        N = math.sqrt(3) * math.sin(k / 3.0)    # Helper Temporary Variable
        P = (b / (3.0 * a)) * -1                # Helper Temporary Variable

        x1 = 2 * j * math.cos(k / 3.0) - (b / (3.0 * a))
        x2 = L * (M + N) + P
        x3 = L * (M - N) + P

        return np.array([x1, x2, x3])           # Returning Real Roots as numpy array.

    elif h > 0:                                 # One Real Root and two Complex Roots
        R = -(g / 2.0) + math.sqrt(h)           # Helper Temporary Variable
        if R >= 0:
            S = R ** (1 / 3.0)                  # Helper Temporary Variable
        else:
            S = (-R) ** (1 / 3.0) * -1          # Helper Temporary Variable
        T = -(g / 2.0) - math.sqrt(h)
        if T >= 0:
            U = (T ** (1 / 3.0))                # Helper Temporary Variable
        else:
            U = ((-T) ** (1 / 3.0)) * -1        # Helper Temporary Variable

        x1 = (S + U) - (b / (3.0 * a))
        x2 = -(S + U) / 2 - (b / (3.0 * a)) + (S - U) * math.sqrt(3) * 0.5j
        x3 = -(S + U) / 2 - (b / (3.0 * a)) - (S - U) * math.sqrt(3) * 0.5j

        return np.array([x1, x2, x3])           # Returning One Real Root and two Complex Roots as numpy array.

def quadratic_solver(a,b,c): 

    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    return np.array([sol1, sol2])

def linear_solver(a,b): 
    
    # ax + b = 0 
    
    return -b/a 

def changeSign(index,x): 
    nums = [0,1,2,3,4,5,6,7,8,9]
    
    for i in range(len(x)): 
    
        if i > index: 
            if x[i] in nums: 
                if x[i-1] == 10: 
                    x[i] = -1*x[i] 

        elif i == index: 
            if x[i] in nums: 
                x[i] = -1*x[i] 

        elif i < index: 
            if x[i] in nums: 
                if x[i-1] == 11: 
                    x[i] = -1*x[i]   

def polyEqSolver(x): 
    printEq(x)
    print('\n ------------------------------\n')
    degree=highdegree(x)
    #equality index
    ind=0
    for i in x:
        if i==12:
            break
        ind=ind+1   
     
    print('Old x:', x)
    x=x[0:ind]+x[ind+1:len(x)] 
    print('New x: ', x) 
    
    #Finding Degree of Polynomial 
    
    degree = highdegree(x) 
    print()
    print('Degree of Polynomial : ', degree) 
    print('\n ------------------------------\n')
    
    #-------------------------------------
    
    changeSign(ind, x) 
    
    print('New x (with sign changes): ', x) 
    print('\n ------------------------------\n')
    
    
    # ------------------------------------
    #Checking degrees of all X's in the equation 
    
    x_degs = [(i-1, x[i-1], x[i+1]) for i, deg in enumerate(x) if (deg == 13 and i !=len(x) - 1)]
    
    #If any of the X doesn't have degree written explicitly (That is, degree = 1) 
    x_degs = x_degs + [(i-1, x[i-1] ,1) for i, deg in enumerate(x) if (deg == 13 and (i == len(x) - 1 or x[i+1] >=10))]
    
    for deg_data in x_degs:
        print('Index of Coefficient: ',  deg_data[0]) 
        print('Coefficient: ', deg_data[1])
        print('Degree: ', deg_data[2]) 
        print() 
        
    print('------------------------------\n') 
    
    # Finding Final Coefficients of Polynomial Equation 
    
    constant = 0
    eq_coeffs = [] 
    
    for k in range(degree + 1): 
        
        #For Constant
        if k == 0: 
            for i, deg in enumerate(x):              
                if deg <10:
                    flag = False 
                    for deg_data in x_degs: 
                        if i == deg_data[0]: 
                            flag = True 
                            break 
                    
                    if flag == False and x[i-1] !=13: 
                        constant += deg 
        
        #For powers of X  
        else: 
            
            coeff_sum = 0 
            for deg_data in x_degs: 
                if deg_data[2] == k: 
                    coeff_sum += deg_data[1] 
            
            eq_coeffs.append(coeff_sum) 
        
    print('Constant: ', constant) 
    print('Coeffs of Equation: ', eq_coeffs) 
        
    print('------------------------------\n') 
    
    #Putting in appropriate Polynomial Solver 
    
    print('Roots of equations are :')
    
    
    #Linear 
    if k == 1:
         return linear_solver(a=eq_coeffs[0], b = constant) 
    
    #Quadratic
    if k == 2:
        return quadratic_solver(a=eq_coeffs[1], b = eq_coeffs[0], c = constant)  
    
    #Cubic
    if k == 3: 
        return cubic_solver(a = eq_coeffs[2], b = eq_coeffs[1], c = eq_coeffs[0], d = constant) 