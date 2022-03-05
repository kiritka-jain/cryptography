import random


def is_prime(num):
    if num <=1:
        return False
    for _ in range(5):
        random_num = random.randint(2, num)-1
        if pow(random_num,num-1,num) != 1:
            return False
    return True


check_num = int(input("Enter the number you want to check:"))
print(is_prime(check_num))
