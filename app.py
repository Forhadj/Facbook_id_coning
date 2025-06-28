#!/usr/bin/python

import os, zlib
from os import system as osRUB
from os import system as cmd
os.system('clear')
print('loading Modules ...\n')

try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')

try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')

from urllib.request import Request, urlopen
import random, platform, sys, subprocess, threading, itertools, base64, uuid, re, json, shutil, webbrowser, time, datetime, string
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from string import *
from random import randint
from time import sleep as slp
from zlib import decompress 

model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()

totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total = []
methods = []
srange = 0
saved = []
filter = []

def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def randBuildvsskj():
    END = '[FBAN/EMA;FBBV/352223683;FBAV/291.0.0.12.110;FBDV/SM-G935FD;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'

logo = """ 
  ______         _               _  
 |  ____|       | |             | | 
 | |__ ___  _ __| |__   __ _  __| | 
 |  __/ _ \| '__| '_ \ / _` |/ _` | 
 | | | (_) | |  | | | | (_| | (_| | 
 |_|  \___/|_|  |_| |_|\__,_|\__,_| 
                                    
                                    
\033[1;37m------------------------------------------------
\033[1;37m Owner   :              Forhad Hasan
\033[1;37m Facebook:           Forhad Hasan 
\033[1;37m Github  :               Forhadj
\033[1;37m Version :            19.8
\033[1;37m------------------------------------------------
"""

def clear():
    os.system("clear")
    print(logo)    

def result(OKs, cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print(47*'-')
        print(' The Process has been Complete...')
        print(' TOTAL OK: %s' % str(len(oks)))
        print(' TOTAL CP: %s' % str(len(cps)))
        print(47*'-')
        input("Press enter to back SSB Menu ")
        exit()

# ... [Rest of the code remains the same with proper indentation and fixes] ...

def main():
    sarfraz()

if __name__ == "__main__":
    main()
