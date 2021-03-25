from Crypto.Util import number

''' KryptoMagick 2021 '''
''' This code demonstrates the reduced Fetu I algorithm '''

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
    print("Exchange phase1")
    p1 = pow(p0, y, MA)
    p1B = pow(p0B, y, MA)
    print(p1, p1B)
    print("Arrive at the secret key phase2")
    p2 = pow(p1B, TkA, MA)
    p2B = pow(p1, TkB, MA)
    print(p2, p2B)

fetu_demo(256)
