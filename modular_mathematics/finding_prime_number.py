from math import sqrt
from math import floor

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num %2 == 0:
        return False
    for n in range(3,floor(sqrt(num))+1,2):
        if num % n == 0:
            return False
    return True
check_num = int(input("Enter the number you want to check:"))
print(is_prime(check_num))