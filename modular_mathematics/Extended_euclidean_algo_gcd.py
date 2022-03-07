def extended_gcd(a, b):
    # base case(gcd = ax+by)
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(a % b, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


a = int(input())
b = int(input())
print(extended_gcd(a, b))
