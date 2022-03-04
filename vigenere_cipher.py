"""
Encryption and decryption program to demonstrate Vigenere-Cipher.
"""

Aplhabets = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def vigenere_encrypt(plain_text, key_val):
    key_val = key_val.upper()
    plain_text = plain_text.upper()
    cipher_text = ''
    key_val_index = 0
    for char in plain_text:
        index = Aplhabets.find(char)+Aplhabets.find(key_val[key_val_index])
        encrypted_val = index % len(Aplhabets)
        cipher_text += Aplhabets[encrypted_val]
        key_val_index +=1
        if key_val_index == len(key_val):
            key_val_index = 0

    return cipher_text


def vigenere_decrypt(cipher_text, key_val):
    key_val = key_val.upper()
    cipher_text = cipher_text.upper()
    plain_text = ''
    key_val_index = 0
    for char in cipher_text:
        index = Aplhabets.find(char) - Aplhabets.find(key_val[key_val_index])
        decrypted_val = index % len(Aplhabets)
        plain_text += Aplhabets[decrypted_val]
        key_val_index += 1
        if key_val_index == len(key_val):
            key_val_index = 0

    return plain_text

given_text = "This is an example"
key = 'SECRET'

cipher_text = (vigenere_encrypt(given_text, key))
print(cipher_text)
print(vigenere_decrypt(cipher_text, key))