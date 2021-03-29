from Crypto.Util import number

''' KryptoMagick 2021 '''
''' This code demonstrates the Fetu A PKD algorithm '''

def FermatPrimeTest(n):
    t = int(n / 2)
    r = pow(t, (n - 1) , n)
    if r == 1:
        return True
    else:
        return False

def nearest_prime(n):
   p = n
   while not FermatPrimeTest(p):
       p += 1
   return p

def genBase(size):
    A = number.getPrime(size)
    B = number.getPrime(size)
    while B == A:
        B = number.getPrime(size)
    return A, B

def keygen(size):
    N, M = genBase(size)
    Tk = number.getRandomRange(1, (M - 1))
    return Tk, N, M

def fetuA_demo(size):
    print("Generating Alice and Bob's keys")
    TkA, nA, MA = keygen(size)
    TkB, nB, MB = keygen(size)
    print(TkA, nA, MA)
    print(TkB, nB, MB)
    print("Exchanging and agreeing upon a public modulus")
    print("Each choose a number in the public modulus")
    y = number.getRandomRange(1, (MA - 1))
    yB = number.getRandomRange(1, (MA - 1))
    print(y, yB)
    print("Compute phase0")
    p0 = pow(nA, TkA, MA)
    p0B = pow(nA, TkB, MA)
    print(p0, p0B)
    print("Exchange phase1")
    p1 = pow(p0, y, MA)
    p1B = pow(p0B, y, MA)
    print(p1, p1B)
    print("Arrive at the secret modulus phase2")
    p2 = pow(p1B, TkA, MA)
    p2B = pow(p1, TkB, MA)
    print(p2, p2B)
    smA = nearest_prime(p2)
    smB = nearest_prime(p2B)
    print("Find the nearest prime to the secret modulus")
    print(smA, smB)
    skA = number.getRandomRange(1, (smA - 1))
    skB = number.getRandomRange(1, (smB - 1))
    print("Generate secret keys in the secret modulus")
    print(skA, skB)
    print("Exchange phase3")
    p3 = pow(nB, skA, smA)
    p3B = pow(nB, skB, smB)
    print(p3, p3B)
    print("Arrive at the shared key phase4")
    p4 = pow(p3B, skA, smA)
    p4B = pow(p3, skB, smB)
    print(p4, p4B)

fetuA_demo(256)
