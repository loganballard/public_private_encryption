from random import randint, seed, getrandbits
from millerrabin import isPrime

GENERATOR = 2   # set default 

# faking 32 bit uints because python is too smart for data
# types
def fake32BitInt(num):
    return num % 4294967295

# Getting a safely generated random prime using millerrabin
# and 2 as a generator
def getPrime(bitLength=31):
    random = 0
    prime = 0
    while not isPrime(prime):
        random = getrandbits(bitLength)
        if random % 12 != 5:
            continue
        prime = (2*random) + 1
    return prime

# get the private key, which will be random number
# between 0 and chosen prime
def getPriKey(userSeed, prime):
    seed(userSeed)
    return randint(0, prime)

# part 3 of public key
def getE2(privateKey, prime, gen=GENERATOR):
    return pow(gen, privateKey, prime)

# the real function we want here
def getKeys(seed=None):
    prime = getPrime()
    priKey = getPriKey(seed, prime)
    e2 = getE2(priKey, prime)
    gen = GENERATOR
    return {
        'priKey': priKey,
        'pubKey': {
            'p': prime,
            'g': gen,
            'e2': e2
        }
    }