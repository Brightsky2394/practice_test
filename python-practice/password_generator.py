#!/usr/bin/python3

import random
import string

total_char = string.ascii_letters + string.digits + string.punctuation
char_len = 16
password = ''.join(random.sample(total_char, char_len))
print(password)
