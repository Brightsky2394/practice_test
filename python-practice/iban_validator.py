#!/usr/bin.python3

iban = input("Enter your IBAN with space between the value: ")
iban = iban.replace(" ", '')
if not iban.isalnum():
    print("You've entered an invalid character")
if len(iban) < 15:
    print("IBAN is too short")
if len(iban) > 31:
    print("IBAN is too long")
else:
    iban = (iban[4:] + iban[:4]).upper()
    iban1 = ''
    for ch in iban:
        if ch.isdigit():
            iban1 += ch
        else:
            iban1 = str(10 + ord(ch) - ord('A'))
    iban = int(iban1)
    if iban % 97 == 1:
        print("IBAN is valid")
    else:
        print("IBAN is invalid")

