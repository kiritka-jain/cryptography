"""
To find the GCD of two numbers

"""
num1 = int(input())
num2 = int(input())


def find_gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    return find_gcd(num2,num1 % num2)


print(find_gcd(num1,num2))