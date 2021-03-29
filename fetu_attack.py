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

def fetu_factor(p, y, m, q):
    x = m % p
    z = p % y
    print(x, z, p)
    while p != y:
        p = ((p + 1) % m)
    p -= 1
    print(p)

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
print("Generating Alice and Bob's keys")
skA, nA, MA = keygen(size)
skB, nB, MB = keygen(size)

print("Alice keys")
print(skA, nA, MA)
print("Bob keys")
print(skB, nB, MB)
print("Generating ephemeral public keys")
TkA = number.getRandomRange(1, (MA - 1))
TkB = number.getRandomRange(1, (MA - 1))
y = number.getRandomRange(1, (MA - 1))
yB = number.getRandomRange(1, (MA - 1))

print(TkA, TkB)
print(y)
p0 = pow(nA, TkA, MA)
p0B = pow(nA, TkB, MA)
print("p0", p0, p0B)
p1 = pow(p0, y, MA)
p1B = pow(p0B, y, MA)
print("p1", p1, p1B)
p2 = pow(p1B, TkA, MA)
p2B = pow(p1, TkB, MA)
#smA = nearest_prime(p2)
#smB = nearest_prime(p2B)
smA = p2
smB = p2B
print("sm", smA, smB)
p3 = pow(nB, skA, smA)
p3B = pow(nB, skB, smB)
print(p3, p3B)
#p3cA = pow(nB, skA, p2)
#p3BcB = pow(nB, skB, p2B)
#print(p3cA, p3BcB)
p4 = pow(p3B, skA, smA)
p4B = pow(p3, skB, smB)
print("sk", p4, p4B)
keylen = len(number.long_to_bytes(p4))
print("keylen", keylen)
print(p1, p1B)
t0 = number.inverse(p1, nA)
print("inverse", t0)
t1 = pow(t0, p1, MA)
print(t1)
x = pow(y, p1, MA)
print("x", x)
Osk = discreteLogarithm(nA, p1, MA)
print("Osk", Osk)
o0 = pow(p1B, Osk, MA)
print(o0)
o1 = pow(o0, Osk, MA)
print(o1)
#print(nB, p3, o1)
#Osk = discreteLogarithm(nB, p3, o1)
#print(Osk)
#o2 = pow(p3B, Osk, o1)
#print(o2)
fetu_factor(p1, y, MA, smA)
