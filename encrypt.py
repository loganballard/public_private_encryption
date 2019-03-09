from random import randint

# pass in a dictionary pubKey which has all three
# public key values, expected in the form: 
# {'p': p, 'g': g, 'e2': e2}
def encryptBlock(pubKey, msg, debug=False):
    k = randint(1, pubKey['p']-1)
    if debug:
        print("DEBUG c1: %d c2: %d" % (pow(pubKey['g'], k, pubKey['p']), (pow(pubKey['e2'], k, pubKey['p']) * msg) % pubKey['p']))
    return {
        'c1': pow(pubKey['g'], k, pubKey['p']),
        'c2': (pow(pubKey['e2'], k, pubKey['p']) * msg) % pubKey['p'] 
    }

def makeMsg(string):
    i = 0
    num = 0
    for c in string[::-1]:
        num += ord(c) << (i*8)
        i += 1
    return num

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

def encryptFile(readPath="test/testText.txt", writePath="test/testEncrypted.txt", pubKeyPath='test/testpubkey.txt', debug=False):
    pk = makePubKeyFromFile(pubKeyPath)
    with open(readPath, 'r', encoding='utf-8') as rf:
        allText = rf.read()
    with open(writePath, 'w') as wf:
        for c in allText:
            cipher = encryptBlock(pk, ord(c), debug)
            wf.write(str(cipher['c1']) + " " + str(cipher['c2']) + "\n")
    

    