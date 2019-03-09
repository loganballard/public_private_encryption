import prompts
from keygen import getKeys
from encrypt import encryptFile

def keyGeneration():
    pubPath = input(prompts.pubKeyWritePath)
    priPath = input(prompts.priKeyWritePath)
    seed = input(prompts.seedPrompt)
    keyDict = getKeys(seed)
    with open(pubPath, 'w') as pubKeyFile:
        pubKeyFile.write(str(keyDict['pubKey']['p']) + "\n")
        pubKeyFile.write(str(keyDict['pubKey']['g']) + "\n")
        pubKeyFile.write(str(keyDict['pubKey']['e2']))
    with open(priPath, 'w') as priKeyFile:
        priKeyFile.write(str(keyDict['priKey']))

def fileEncrypt():
    plainPath = input(prompts.plainTextFile)
    encWritePath = input(prompts.encTextFileWrite)
    pubKeyPath = input(prompts.pubKeyReadPath)
    encryptFile(plainPath, encWritePath, pubKeyPath)

def fileDecrypt():
    pass

def quitWithError():  
    print('Please select a real option (1,2,3)!')
    exit(0)

def collectInput():
    choice = input(prompts.screenOne)
    try:
        choice = int(choice)
    except ValueError:
        quitWithError()
    if choice == 1:
        keyGeneration()
    elif choice == 2:
        fileEncrypt()
    elif choice == 3:
        fileDecrypt()
    else:
        quitWithError()