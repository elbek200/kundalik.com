import hashlib

from database2 import *


def hashcode(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    return sha256.hexdigest()

def admin():
    n = input("[1] - kurs qoshish , [2] - kurslarga yozilgan o'quvchilarni korish")
    if n == "1" :
        admin_enter_kurs()
    elif n == "2" :
        kursga_yozilgan_korish()
    else :
        print ("Invalid code")

def oquvchi(username):
    n = input("[1] - kurslar royhati , [2] - kursga yozilish , [3] - yozilgan kurslar royhati \n --> : " )
    if n == "1" :
        kurslar()
    elif n == "2" :
        kursga_yozilish()
    elif n == "3" :
        yoz_kur_roy(username)
    else:
        print ("Invalid code ")
