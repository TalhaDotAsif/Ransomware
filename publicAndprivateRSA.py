from Crypto.PublicKey import RSA           #importing RSA algorithm 
from Crypto.Cipher import AES,PKCS1_OAEP   #importing AES-128 and padding for RSA algorithm
import base64

key=RSA.generate(2048)                    #creating an object "key" and 2048 represents the RSA's strength
privateKeyVal=key.export_key()              #export_key() is function of RSA that will give the private key by default
with open('private.txt','wb') as t:       #writing private file so that it can be used by Attacker
    t.write(privateKeyVal)                  
publicKeyVal=key.publickey().export_key()   #for public key, which  is stored in variable
with open('public.txt','wb') as t:        #writing to public.txt
    t.write(publicKeyVal)

with open('testing.txt','wb') as t:
    t.write(publicKeyVal)

    