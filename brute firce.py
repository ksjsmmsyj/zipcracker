import itertools
import time
import zipfile

def tryPassword( stringTypeSet, filename):
    start = time.time()
    zf=zipfile.ZipFile(filename)
    chars = stringTypeSet
    attempts = 0
    for i in range(1, 9):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            try:
            	zf.extractall(pwd=bytes(letter, 'utf-8'))
            	print(attempts)
           
            	
            	print('Your password is', letter)
            	
            	
            	return
            	 
            except:
            	
            	a="false"
            	
            if a!="false":
           	 print(letter)
            
            	
sfile=input("Enter file name:")
           	
stri="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#?_&-+()/?!;"
tryPassword(stri, sfile)            					
