# Simple Public-Private Key Encryption Algorithm

## Basics
Keys are generated via some element of entropy (random integer) as well as tenenats of mod math.  Note that these keys will be cryptographically insecure as they are 32 bits, could easily be scaled to 128, 256, 512, 1024, and beyond.  Messages are encrypted using private keys and exchanged with public keys.  Messages are decrypted using a shared session key (prime number value).  This algorithm is based on the Diffie-Hellman protocol.

## Dependencies:
* Python

## Use
The supplied driver will walk the user through the necessary steps.

From within the root directory:
`python driver.py`

## Example
#### Key Pair Creation

```
PS C:\Users\logan\Documents\School-Related\MS\Winter 2019\Cryptography\project 2\simple-symmetric> python .\driver.py
Debug Mode [Y/N]?:N

Please select an option [1, 2, 3, or 4]:
    1. Create Key Pair
    2. Encrypt a File
    3. Decrypt a File
    4. Exit
1

Enter the filepath (relative or absolute) to write the public key file to:
example/pubkey.txt

Enter the filepath (relative or absolute) to write the private key file to:
example/prikey.txt

Enter some garbage to seed the random number generator (seriously, anything):
the quick brown fox jumpedo ver the last dog
```

Private key:
```
2484644363
2
1299615758
```

Public Key:
```
2484644363
2
2055228143
```

### Encrypt
```Please select an option [1, 2, 3, or 4]:
    1. Create Key Pair
    2. Encrypt a File
    3. Decrypt a File
    4. Exit
2

Enter the filepath (relative or absolute) to read the plaintext from:
test/testText.txt

Enter the filepath (relative or absolute) to write the encrypted text file to:
example/enc.txt

Enter the filepath (relative or absolute) to read the public key file from:
example/pubkey.txt
```

Plaintext:
```
17. Art forms that appeal to modern leftish intellectuals tend to focus on sordidness, defeat and despair, or else they take an orgiastic tone, throwing off rational control as if there were no hope of accomplishing anything through rational calculation and all that was left was to immerse oneself in the sensations of the moment.

18. Modern leftish philosophers tend to dismiss reason, science, objective reality and to insist that everything is culturally relative. It is true that one can ask serious questions about the foundations of scientific knowledge and about how, if at all, the concept of objective reality can be defined. But it is obvious that modern leftish philosophers are not simply cool-headed logicians systematically analyzing the foundations of knowledge. They are deeply involved emotionally in their attack on truth and reality. They attack these concepts because of their own psychological needs. For one thing, their attack is an outlet for hostility, and, to the extent that it is successful, it satisfies the drive for power. More importantly, the leftist hates science and rationality because they classify certain beliefs as true (i.e., successful, superior) and other beliefs as false (i.e., failed, inferior). The leftist’s feelings of inferiority run so deep that he cannot tolerate any classification of some things as successful or superior and other things as failed or inferior. This also underlies the rejection by many leftists of the concept of mental illness and of the utility of IQ tests. Leftists are antagonistic to genetic explanations of human abilities or behavior because such explanations tend to make some persons appear superior or inferior to others. Leftists prefer to give society the credit or blame for an individual’s ability or lack of it. Thus if a person is “inferior” it is not his fault, but society’s, because he has not been brought up properly.
```

Encrypted:
```
2317418934 167306341
(...)
2193715459 1092633621
```

### Decryption

```Please select an option [1, 2, 3, or 4]:
    1. Create Key Pair
    2. Encrypt a File
    3. Decrypt a File
    4. Exit
3

Enter the filepath (relative or absolute) to read the encrypted file from:
example/enc.txt

Enter the filepath (relative or absolute) to write the decrypted text file to:
example/dec.txt

Enter the filepath (relative or absolute) to read the private key file from:
example/prikey.txt
```

Decryption:
```
17. Art forms that appeal to modern leftish intellectuals tend to focus on sordidness, defeat and despair, or else they take an orgiastic tone, throwing off rational control as if there were no hope of accomplishing anything through rational calculation and all that was left was to immerse oneself in the sensations of the moment.

18. Modern leftish philosophers tend to dismiss reason, science, objective reality and to insist that everything is culturally relative. It is true that one can ask serious questions about the foundations of scientific knowledge and about how, if at all, the concept of objective reality can be defined. But it is obvious that modern leftish philosophers are not simply cool-headed logicians systematically analyzing the foundations of knowledge. They are deeply involved emotionally in their attack on truth and reality. They attack these concepts because of their own psychological needs. For one thing, their attack is an outlet for hostility, and, to the extent that it is successful, it satisfies the drive for power. More importantly, the leftist hates science and rationality because they classify certain beliefs as true (i.e., successful, superior) and other beliefs as false (i.e., failed, inferior). The leftist’s feelings of inferiority run so deep that he cannot tolerate any classification of some things as successful or superior and other things as failed or inferior. This also underlies the rejection by many leftists of the concept of mental illness and of the utility of IQ tests. Leftists are antagonistic to genetic explanations of human abilities or behavior because such explanations tend to make some persons appear superior or inferior to others. Leftists prefer to give society the credit or blame for an individual’s ability or lack of it. Thus if a person is “inferior” it is not his fault, but society’s, because he has not been brought up properly.
```