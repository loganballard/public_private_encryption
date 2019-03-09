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
    done = False
    prime = 0
    while not done:
        random = getrandbits(bitLength)
        if (random % 12) != 5:
            continue
        prime = (2*random) + 1
        if isPrime(prime) and prime > 2147483648:
            done = True
    return prime

# get the private key, which will be random number
# between 1 and chosen prime-2
def getPriKey(userSeed, prime):
    seed(userSeed)
    return randint(1, prime-2)

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
        'd': priKey,
        'p': prime,
        'g': gen,
        'e2': e2
    }