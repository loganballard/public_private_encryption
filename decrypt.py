# give a private key file path, read in and create
# the prikey dictionary
def makePriKeyFromFile(pubKeyFile):
    with open(pubKeyFile, 'r') as pkf:
        pubKeyList = pkf.readlines()
    return int(pubKeyList[2]), int(pubKeyList[0])

# decryption based on fermats little theorum
# takes private key, c1, c2, prime as ints
def decryptBlock(priKey, c1, c2, prime):
    return (pow(c1, prime-1-priKey, prime) * (c2 % prime)) % prime

def decryptFile(readPath="test/testEncrypted.txt", writePath="test/testDecrypted.txt", priKeyPath='test/testprikey.txt', debug=False):
    priKey, prime = makePriKeyFromFile(priKeyPath)
    with open(readPath, 'r') as rf:
        allCipherLines = rf.readlines()
    with open(writePath, 'w', encoding='utf-8') as wf:
        output = ''
        for line in allCipherLines:
            c1c2 = line.split()
            c1 = int(c1c2[0])
            c2 = int(c1c2[1])
            output += chr(decryptBlock(priKey, c1, c2, prime))
        if debug:
            print("DEBUG decrypted output: \n%s\n" % output)
        wf.write(output)