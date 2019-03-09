# faking 32 bit uints because python is too smart for data
# types
def fake32BitInt(num):
    return num % 4294967295

# decryption based on fermats little theorum
# takes private key and ciphertext msg as input
# private key is a 32-bit uint, ciphertext msg
# a dict of form:
#   {'c1': c1, 'c2': c2}
def decrypt(priKey, ciphertext, prime):
    left = pow(ciphertext['c1'], prime-1-priKey, prime)
    right = ciphertext['c2'] % prime
    return (left * right) % prime 