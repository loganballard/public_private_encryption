from random import randint

# faking 32 bit uints because python is too smart for data
# types
def fake32BitInt(num=0):
    return num % 4294967295

# pass in a dictionary pubKey which has all three
# public key values, expected in the form: 
# {'p': p, 'g': g, 'e2': e2}
def encryptBlock(pubKey, msg):
    k = randint(0, pubKey['p'])
    cipher = {
        'c1': pow(pubKey['g'], k, pubKey['p']),
        'c2': pow(fake32BitInt(pubKey['e2']*msg), k, pubKey['p'])
    }
    return cipher

# give a public key file path, read in and create
# the pubkey dictionary
def makePubKeyFromFile(pubKeyFile):
    pk = {}
    with open(pubKeyFile, 'r') as pkf:
        pubKeyList = pkf.readlines()
    pk['p'] = int(pubKeyList[0])
    pk['g'] = int(pubKeyList[1])
    pk['e2'] = int(pubKeyList[2])
    return pk

def encryptFile(readPath="test/testText.txt", writePath="test/testEncrypted.txt", pubKeyPath='test/testpubkey.txt'):
    pk = makePubKeyFromFile(pubKeyPath)
    with open(readPath, 'r', encoding='utf-8') as rf:
        allText = rf.read()
    with open(writePath, 'w') as wf:
        for c in allText:
            cipher = encryptBlock(pk, ord(c))
            wf.write(str(cipher['c1']) + " " + str(cipher['c2']) + "\n")
    

    