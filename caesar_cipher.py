"""
Encryption and decryption program to demonstrate Ceaser-Cipher.
"""

Aplhabets = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def ceaser_encrypt(plain_text, key_val):
    cipher_text = ''
    plain_text = plain_text.upper()
    for char in plain_text:
        index = Aplhabets.find(char)
        encrypted_val = (index + key_val) % (len(Aplhabets))
        cipher_text += Aplhabets[encrypted_val]
    return cipher_text


def ceaser_decrypt(cipher_text, key_val):
    plain_text = ''
    cipher_text = cipher_text.upper()
    for char in cipher_text:
        index = Aplhabets.find(char)
        decrypted_val = (index - key_val) % (len(Aplhabets))
        plain_text += Aplhabets[decrypted_val]
    return plain_text


given_text = "This is an example"
key = 4

cipher_text = (ceaser_encrypt(given_text, key))
print(cipher_text)
print(ceaser_decrypt(cipher_text, key))
