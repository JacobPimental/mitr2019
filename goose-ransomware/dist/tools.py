import requests

def viginere_xor_decrypt(key, cipher):
    i = 0
    l = []
    for b in cipher:
        n = b ^ key[i%len(key)]
        l.append(n)
        i += 1
    return l

def write_file(dat):
    new_file = open('test','wb')
    for b in dat:
        new_file.write(bytes(chr(b), 'utf-8'))

f = open('decoded_encrypted_lua', 'rb')
dat = f.read()

r = requests.get('https://pastebin.com/raw/LHS242K1')
poem = bytes(r.text, 'utf-8')
