KEY = 'abcdefghijklmnopqrstuvwxyz'

prime = [0,1,3,5,7,9,11,15,17,19,21,25]

def decrypt(a,b,ciphertext):
    result = ''
    
    for x in ciphertext:
        index = KEY.index(x)
        i = ((index * a) + b) % 26
        result = i
    return result
    
for n in range(0,26):
    for x in range(0,26):
        if x in prime:
            dec1 = decrypt(n,x,'c')
            dec2 = decrypt(n,x,'k')
            dec3 = decrypt(n,x,'q')
            dec4 = decrypt(n,x,'b')
            dec5 = decrypt(n,x,'q')
            dec6 = decrypt(n,x,'y')
            print ("A = %d B = %d. %s%s%s%s%s%s" % (n,x,chr(dec1 + 97),chr(dec2 + 97),chr(dec3 + 97),
            chr(dec4 + 97),chr(dec5 + 97),chr(dec6 + 97)))
