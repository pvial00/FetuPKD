#gaaaha Python3 program to calculate  
# discrete logarithm  
import math; 

# Iterative Function to calculate  
# (x ^ y)%p in O(log y)  
def powmod(x, y, p):  
  
    res = 1; # Initialize result  
  
    x = x % p; # Update x if it is more  
               # than or equal to p  
  
    while (y > 0):  
          
        # If y is odd, multiply x with result  
        if (y & 1):  
            res = (res * x) % p;  
  
        # y must be even now  
        y = y >> 1; # y = y/2  
        x = (x * x) % p;  
    return res;  
  
# Function to calculate k for given a, b, m  
def discreteLogarithm(a, b, m):
    n = int(math.sqrt(m) + 1);

    value = [0] * m;

    # Store all values of a^(n*i) of LHS  
    for i in range(n, 0, -1):
        value[ powmod (a, i * n, m) ] = i;

    for j in range(n):

        # Calculate (a ^ j) * b and check  
        # for collision  
        cur = (powmod (a, j, m) * b) % m;

        # If collision occurs i.e., LHS = RHS  
        if (value[cur]):
            ans = value[cur] * n - j;

            # Check whether ans lies below m or not  
            if (ans < m):
                return ans;

    return -1;

def fetu_factor(a, b, m):
    x = m % a
    print(x)

from Crypto.Util import number

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

size = 16
alice_pk = 56843
alice_m = 65011

bob_pk = 42821
bob_m = 40559

print("Alice keys - Alice's Public M was chosen: ")
print(alice_pk, alice_m)
print("Bob keys: ")
print(bob_pk, bob_m)
y = 4331
p1 = 56178
p1B = 42569
p3 = 7131
p3B = 5001
print("Public Y: ")
print(y)
print("Exchange phase1")
print(p1, p1B)
print("Exchange phase3")
print(p3, p3B)
print("Solve for the secret modulus phase2 and the secret key phase4")
print("Alice encrypts a message to Bob by multiplying the plaintext with the secret key")
print("Cipher text")
ctxt = 380556
print(ctxt)
fetu_factor(p1, y, alice_m)
