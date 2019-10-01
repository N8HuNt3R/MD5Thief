#!/user/bin/python

from termcolor import colored
import hashlib

def tryOpen(wordlist):
    global pass_file
    try:
        pass_file = open(wordlist, "r")
    except:
        print("[!!] No Such File At This Path! ")
        quit()

pass_hash = input("[*] Enter MD5 Hash Value: ")
wordlist = input("[*] Enter Passlist Here: ")
tryOpen(wordlist)

for word in pass_file:
    print(colored("[-] trying: " + word.strip("\n"), 'red'))
    enc_wrd = word.encode('utf-8')
    md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    if md5digest == pass_hash:
        print(colored("[+] password has been cracked: " + word, 'green'))
        exit(0)
print("[!] Did not find the password in list! ")
