import random


def generate_key(n, g):
    sender_private_key = random.randint(1, n)
    receiver_private_key = random.randint(1, n)
    k1 = pow(g, sender_private_key, n)
    k2 = pow(g, receiver_private_key, n)
    sender_key = pow(k2, sender_private_key, n)
    receiver_key = pow(k1, receiver_private_key, n)
    return sender_key, receiver_key

n= int(37)
g = int(13)
print(generate_key(n,g))