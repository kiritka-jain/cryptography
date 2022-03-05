from math import floor, sqrt

check_num = int(input("Enter the number"))


def all_factors(num):
    factors = []
    for n in range(2,floor(sqrt(num))):
        if num % n == 0:
            factors.append([n,num/n])
    return factors


print(all_factors(check_num))