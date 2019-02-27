from Crypto.Cipher import DES3, Blowfish
import base64
import pyDes

keys = []
with open("keys.txt") as f:
    for l in f.readlines():
        keys.append(l.strip())

a = 0
for k in keys:
    try:
        f = open("important-file.png.enc", 'rb')
        b = f.read()
        b = base64.b64decode(b)
        iv = b[:8]
        b64k = base64.b64decode(k)
        d = DES3.new(b64k, DES3.MODE_CFB, iv)
        #blow = Blowfish.new(b64k, Blowfish.MODE_CFB)
        plain = d.decrypt(b[8:])
        #plain = base64.b64decode(plain)
        o = open("dec/key" + str(a), '+wb')
        o.write(plain)
        o.close()
        a += 1
    except Exception as e:
        print("Key: " + k)
        print(e)
