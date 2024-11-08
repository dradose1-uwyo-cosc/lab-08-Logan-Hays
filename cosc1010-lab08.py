# Logan Hays
# UWYO COSC 1010
# Submission Date 11/07/2024
# Lab 08
# Lab Section: 13
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


num = input("Please enter a number")

def string_converter(num):
    is_neg = False
    if "-" in num:
        is_neg = True
        num = num.replace("-","")
    if "." in num:
        num_list=num.split(".")
        if len(num_list) == 2 and num_list[0].isdigit() and num_list[1].isdigit():
            if is_neg:
                return -1 * float(num)
            else:
                return float(num)
    elif num.isdigit():
        if is_neg:
            return -1 * int(num)
        else:
            return int(num)
    else:
        return False
    
print(string_converter(num))


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

y_values = []

while True:
    m = input("Type exit to quit or enter your slope?")
    if m.lower() == "exit":
        break 
    else:
        slope = string_converter(m)
    b = input("Type exit to quit or enter your y_intercept?")
    if b.lower() == "exit":
        break 
    else:
        y_intercept = string_converter(b)
    lb = input("Type exit to quit or enter your lower bound")
    if lb.lower() == "exit":
        break 
    else:
        lower_bound = string_converter(lb)
    ub = input("Type exit to quit or enter your upper bound")
    if ub.lower() == "exit":
        break 
    else:
        upper_bound = string_converter(ub)


def slope_values(y_values):
    if lower_bound > upper_bound:
        print("upper bound is lower than lower bound")
        return None
    if lower_bound < upper_bound:
        for x in range(lower_bound, upper_bound +1):
            y = x * slope + y_intercept
            y_values.append(y)
        return y_values

print(slope_values(y_values))

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null




while True:
    first_val = input("Type exit to quit or enter your first value(a)")
    if first_val.lower() == "exit":
        break
    else:
        a = string_converter(first_val)
    second_val = input("Type exit to quit or enter your second value(b)")
    if second_val.lower() == "exit":
        break
    else:
        b = string_converter(second_val)
    third_val = input("Type exit to quit or enter your third value(c)")
    if third_val.lower() == "exit":
        break
    else:
        c = string_converter(third_val)
   

def quad_solve(a,b,c):
    if a == 0:
        print("a can not be 0")
        return None, None
    square_values = (b**2 - 4*a*c)
    if square_values < 0:
        print("null")
        return None, None
    squared_values = square_values ** (1/2)
    neg_b = b * -1
    positive_solution =  (neg_b + squared_values) / (2*a)
    negative_solution = (neg_b - squared_values) / (2*a)
    return positive_solution, negative_solution

if a != False and b != False and c != False:
    positive_solution, negative_solution = quad_solve(a, b, c)
    if positive_solution is not None and negative_solution is not None:
        if positive_solution == negative_solution:
            print(f"The solution is x = {positive_solution}")
        else:
            print(f"The solutions are x = {positive_solution} or x = {negative_solution}")
else:
    print("Invalid input detected. Please enter valid numerical values.")