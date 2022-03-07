import random
from math import floor
from math import sqrt

RANDOM_START = int(1e3)
RANDOM_END = int(1e5)


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, floor(sqrt(num))):
        return False
    return True


def find_gcd(a, b):
    # base case
    if a % b == 0:
        return b
    return find_gcd(b, a % b)


def modular_inverse(a, b):
    # base case(gcd = ax+by)
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = modular_inverse(a % b, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def generate_large_prime_num(num_start=RANDOM_START, num_end=RANDOM_END):
    # generate random number
    random_num = random.randint(num_start, num_end)
    # check if number is prime or not
    while not is_prime(random_num):
        random_num = random.randint(num_start, num_end)
    return random_num


def generate_rsa_keys():
    p = generate_large_prime_num()
    q = generate_large_prime_num()

    # trapdoor operation : multiplying is fast but getting p and q is slow
    n = p * q

    # Euler's totient phi function
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)

    # to find coprime
    while find_gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # modular inverse of e
    d = modular_inverse(e, phi)[1]
    return (d, n), (e, n)


def encrypt(public_key, plain_text):
    e, n = public_key
    cipher_text = []
    for characters in plain_text:
        a = ord(characters)
        cipher_text.append(pow(a, e, n))
    return cipher_text


def decrypt(private_key, cipher_text):
    d, n = private_key
    plain_text = ''
    for num in cipher_text:
        a = pow(num, d, n)
        plain_text += str(chr(a))
    return plain_text


if __name__ == '__main__':
    private_key, public_key = generate_rsa_keys()

    message = "This is an example"
    print("Original message is %s" % message)
    cipher = encrypt(public_key, message)
    print("This is cipher text: %s" % cipher)
    plain = decrypt(private_key, cipher)
    print("This is decrypted message: %s" % plain)
