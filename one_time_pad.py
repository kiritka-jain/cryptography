"""
Encryption and decryption program to demonstrate OTP( One Time Pad).
"""
import random

Aplhabets = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def random_key_generator(plain_text_len):
    random_key = []
    for _ in range(plain_text_len):
        random_key.append(random.randint(0, len(Aplhabets)))
    return random_key


def otp_encrypt(plain_text, key_val):
    plain_text = plain_text.upper()
    cipher_text = ''
    key_val_index = 0
    for index, character in enumerate(plain_text):
        key_index = key_val[index]
        char_imdex = Aplhabets.find(character)
        cipher_text += Aplhabets[(char_imdex + key_index) % len(Aplhabets)]

    return cipher_text


def otp_decrypt(cipher_text, key_val):
    plain_text = ''
    for index, char in enumerate(cipher_text):
        key_index = key_val[index]
        cipher_imdex = Aplhabets.find(char)
        plain_text += Aplhabets[(cipher_imdex - key_index) % len(Aplhabets)]

    return plain_text


given_text = "This is an example"
plain_text_len = len(given_text)
key = random_key_generator(plain_text_len)

cipher_text = (otp_encrypt(given_text, key))
print(cipher_text)
print(otp_decrypt(cipher_text, key))
