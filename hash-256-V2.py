from hashlib import sha256
from hashlib import sha512
from time import sleep
from os import system


print("Start")
sleep(1)
system("cls" or "clear")


def a():
    while True:
        s = input(str('Enter your text?'))
        a = sha256(b"%s" % s.encode()).hexdigest()
        print (a)
    


def b():
    while True:
        s = input(str('Enter your text?'))
        a = sha512(b"%s" % s.encode()).hexdigest()
        print (a)

print ('©Converts any text into a hash©')

print ('hash-256= 1 hash-512= 2')
w = int(input('waht number?'))
system("cls" or "clear")

if w == 1:
    a()
elif w == 2:
    b()

1
