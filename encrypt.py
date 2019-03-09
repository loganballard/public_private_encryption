from random import randint

# faking 32 bit uints because python is too smart for data
# types
def fake32BitInt(num=0):
    return num % 4294967295

# pass in a dictionary pubKey which has all three
# public key values, expected in the form: 
# {'p': p, 'g': g, 'e2': e2}
def encrypt(pubKey, msg):
    k = randint(0, pubKey['p'])
    cipher = {
        'c1': pow(pubKey['g'], k, pubKey['p']),
        'c2': pow(fake32BitInt(pubKey['e2']*msg), k, pubKey['p'])
    }
    return cipher
