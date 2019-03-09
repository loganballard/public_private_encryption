"""
The decryption algorithm works as follows: To decrypt a ciphertext (C1, C2) with her private key d, Alice computes:
•	(C1d)-1C2 mod p = m 		(that is the inverse of C1d mod p times C2)
The inverse for C1 exists because, in general, x has a multiplicative inverse in Zn if x is relatively prime to n. Since p is prime then Zp = {1, …, p-1} and all of these values (the set of possible messages and ciphertext) are relatively prime to p.
The decryption algorithm produces the intended message, because
(C1d)-1∙C2 (mod p) ≡ ((gk)d )-1∙e2k∙m ≡ (gd k)-1∙e2k∙m ≡ ((gd)k)-1∙e2k∙m ≡ (e2k)-1∙e2k ∙m ≡ 1∙m = m.
This works because the definition of inverses gives that, (x)-1∙x mod p = 1 and so we get that (x)-1∙x∙m mod p = m as long as m < p.	

Recommended method for decryption: There is an easier way to compute the decryption. Instead of using m = (C1d)-1∙C2 mod p for decryption, we can avoid the calculation of multiplicative inverse and use m = C1p-1- d C2 mod p. This comes from Fermat’s Little Theorem: If p is a prime and a < p then ap-1 ≡ 1(mod p). So now the decryption algorithm works as follows: To decrypt a ciphertext (C1, C2) with her private key d, Alice computes:
•	C1p-1- d∙C2 mod p = m 		
The calculation is now ((C1p-1-d mod p)(C2 mod p)) mod p = m. 	
"""