from hashlib import sha256
print ('Converts any text into a hash©')
def a():
    s = input(str('Enter your text?'))
    a = sha256(b"%s" % s.encode()).hexdigest()
    print (a)

if 1 == 1:
    a()
