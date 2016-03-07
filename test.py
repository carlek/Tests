import string
import random

MAPPING = {}

def get_map_key():
    # all the allowable characters
    shorty_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    base = len(shorty_chars)

    # generate a random integer. method: e.g. 0.437385979372 --> 437385979372)
    # TODO: for python 2.7 use long(str(random.random())[2:])
    s = str(random.random())[2:]
    if 'e' in s:  # handle numbers like 0.02342300e-05
        s = s[:-4]
    rand_int = int(s)
    # turn that random integer into a string based on the shorty characters
    # basically this is a conversion of base 10 to base"shorty" e.g. 12881221161133516 --> UFnvJhV96
    result = ''
    while rand_int:
        i = rand_int % base
        result += shorty_chars[i]
        rand_int //= base

    # v2.0 return the smallest string not yet in the MAPPING
    for i in range(1, len(result)):
        if result[:i] not in MAPPING:
            return result[:i]

for i in range(1000000):
    key = get_map_key()
    MAPPING[key] = i

print(len(max(MAPPING, key=len)))
print(len(MAPPING))