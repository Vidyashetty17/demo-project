def add (a,b):
    return f"Sum of {a} and {b} is {a+b}"
def sub(a,b):
    if b ==0:
        return "Error: Division by zero"      
    elif b<a:
        return "b should be greater than a"  
    else:
        return a-b