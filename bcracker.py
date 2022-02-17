#!/usr/bin/env python

import threading
import bcrypt
import sys
import os



file = open('pfile.txt', 'r') #This is your wordlist
lines = file.readlines()
 


def brute():
	passwdstr=line.strip()
	passwd =passwdstr.encode('UTF-8')
	salt=b'$2b$12$o9zj/IH7Sx/qYY2e7OcRHu' #It doesn't matter, so don't change.
	hashed = b'$2a$10$oXdjzyD.JL0LEv1LPCCAFebNCoAWQ2drucMGBN3xAxLfjVoiS7cdC' #your bcrypt hash here.
	if bcrypt.checkpw(passwd, hashed):
		print(f"Hash Cracked Successfully. Your Password is {passwdstr}.......................................\n")
		os._exit(0)
		print()
	else:
		sys.stdout.write(f"{passwdstr} does not match this hash.{c} passwords tried so far. \033[0m\033[0K\r")
		


threads = []




c= 0
for line in lines:
	c += 1
	thread = threading.Thread(target = brute)
	thread.start()
	threads.append(thread)


for thread in threads:
   	thread.join()
   


