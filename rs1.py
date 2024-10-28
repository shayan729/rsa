import random

def gcd(a,b):
    while b!=0:
        a,b =b, a % b
    return a;
    
def inverse(e,phi):
    return pow(e,-1,phi)
    
def is_prime(num):
    if num < 2:
        return False;
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False;
    return True;


def keyGenerator(p,q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p and q must be prime.");
    elif p == q:
        raise ValueError("p and q cannot be equal");
        
    n = p * q;
    phi = (p-1) * (q-1);
    
    e = random.randrange(2,phi)
    g = gcd(e,phi)
    while g != 1:
        e = random.randrange(2,phi)
        g = gcd(e, phi);
    d = inverse(e,phi)
    return ((e,n), (d,n))

def encrypt(pk, message):
    key,n = pk
    cipherText = [pow(ord(char), key, n) for char in message]
    return cipherText;

def decrypt(pk, ciphertext):
    key,n = pk
    plan = [ chr(pow(char, key, n )) for char in ciphertext] 
    return ''.join(plan);

def RSA():
    p=17;
    q=19;
    public, private = keyGenerator(p,q);
    print(f"Public Key: {public} \nPrivate key: {private}");
    message = "Hello Jenix by RSA!";
    print("Original Messsage:",message);
    enc_mess = encrypt(public,message);    
    print("encrypted message:",enc_mess);
    dec_mess = decrypt(private,enc_mess);
    print("Decrypted message:",dec_mess);
    
RSA();