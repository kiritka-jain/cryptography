"""
    Modular inverse function using brute force method.It's time complexity is expotential.
"""

def modular_inverse(a,m):
    for i in range(1,m-1):
        if (a*i)%m == 1:
            return i
    return print("No modular inverse exisit for the given value.")

print(modular_inverse(9,31))