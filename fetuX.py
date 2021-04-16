from Crypto.Util import number

''' KryptoMagick 2021 '''
''' This code demonstrates the reduced Fetu X algorithm '''

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

def fetu_demo(size, itera=100000):
    print("Generating Alice and Bob's keys")
    skA, nA, MA = keygen(size)
    skB, nB, MB = keygen(size)
    T = 2
    print(skA, nA, MA)
    print(skB, nB, MB)
    print("Exchanging and agreeing upon a public modulus")
    print("Compute phase0")
    p0 = pow(nA, skA, MA)
    p0B = pow(nA, skB, MA)
    print(p0, p0B)
    print("Exchange phase1")
    p1 = pow(p0, T, MA)
    p1B = pow(p0B, T, MA)
    for x in range(itera):
        p1 = pow(p1, T, MA)
        p1B = pow(p1B, T, MA)
        print(p1, p1B)
    p2 = pow(p1, nA, MA)
    p2B = pow(p1B, nA, MA)
    print(p2, p2B)
    print("Arrive at the secret key phase2")
    p3 = pow(p2B, skA, MA)
    p3B = pow(p2, skB, MA)
    print(p3, p3B)

fetu_demo(256)
