#!/usr/bin/python3

text = input("Enter message of your choice: ")

def encrypt_message():
    cipher_ept = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher_ept += chr(code)
    print(cipher_ept)

encrypt_message()


def decrypt_message():
    cipher_dpt = ''
    for ch in text:
        if not ch.isalpha():
            continue
        ch = ch.upper()
        code = ord(ch) - 1
        if code < ord('A'):
            code = ord('Z')
        cipher_dpt += chr(code)
    print(cipher_dpt)

decrypt_message()
