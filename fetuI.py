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
    print("Compute phase0")
    p0 = pow(nA, skA, MA)
    p0B = pow(nA, skB, MA)
    print(p0, p0B)
    print("Exchange phase1")
    p1 = pow(p0, nA, MA)
    p1B = pow(p0B, nA, MA)
    print(p1, p1B)
    print("Arrive at the secret key phase2")
    p2 = pow(p1B, skA, MA)
    p2B = pow(p1, skB, MA)
    print(p2, p2B)

fetu_demo(256)
