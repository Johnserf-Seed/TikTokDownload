import time
import random

def create_s_v_web_id():
    e = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    t = len(e)
    n = base36_encode(int(time.time()*1000))   # Convert timestamp to base 36

    r = [''] * 36
    r[8] = r[13] = r[18] = r[23] = "_"
    r[14] = "4"

    for i in range(36):
        if not r[i]:
            o = int(random.random() * t)
            r[i] = e[3 & o | 8 if i == 19 else o]

    return "verify_" + n + "_" + "".join(r)

def base36_encode(number):
    """Converts an integer to a base36 string."""
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    base36 = []

    while number:
        number, i = divmod(number, 36)
        base36.append(alphabet[i])

    return ''.join(reversed(base36))

print(create_s_v_web_id())