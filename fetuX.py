from Crypto.Util import number

''' KryptoMagick 2021 '''
''' This code demonstrates the Fetu X algorithm '''

def genBase(size):
    A = number.getPrime(size)
    B = number.getPrime(size)
    while B == A:
        B = number.getPrime(size)
    return A, B

def keygen(size):
    N, M = genBase(size)
    sk = number.getRandomRange(1, (M - 1))
    return sk, N, M

def fetu_demo(size):
    print("Generating Alice and Bob's keys")
    skA, nA, MA = keygen(size)
    skB, nB, MB = keygen(size)
    print(skA, nA, MA)
    print(skB, nB, MB)
    print("Exchanging and agreeing upon a public modulus")
    print("Each choose a number in the public modulus")
    y = number.getRandomRange(1, (MA - 1))
    yB = number.getRandomRange(1, (MA - 1))
    print(y, yB)
    print("Each choose a temporary key in the public modulus")
    TkA = number.getRandomRange(1, (MA - 1))
    TkB = number.getRandomRange(1, (MA - 1))
    print(TkA, TkB)
    print("Compute phase0")
    p0 = pow(nA, TkA, MA)
    p0B = pow(nA, TkB, MA)
    print(p0, p0B)
    print("Compute phase1")
    p1 = pow(p0, y, MA)
    p1B = pow(p0B, nB, MA)
    print(p1, p1B)
    print("Exchange phase2")
    p2 = pow(p1, nB, MA)
    p2B = pow(p1B, y, MA)
    print(p2, p2B)
    print("Arrive at the secret key phase3")
    p3 = pow(p2B, TkA, MA)
    p3B = pow(p2, TkB, MA)
    print(p3, p3B)

fetu_demo(16)
