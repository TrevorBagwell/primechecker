from math import sqrt

def isPrime(k,known):
    """assumes k is odd and known includes odd primes <= sqrt(p)"""
    s = sqrt(k)
    for p in known:
        if k % p == 0:
            return False
        elif p > s:
            return True

def primes():
    yield 2
    yield 3
    yield 5
    known = [5] #known odd primes > 3. Iteration skips multiples of 3
    candidate = 7
    parity = 1

    while True:
        while not isPrime(candidate,known):
            candidate += (2 + 2*parity)
            parity = 1 - parity
        yield candidate
        known.append(candidate)
        candidate += (2 + 2*parity)
        parity = 1 - parity



def fib():
    yield 1
    a = 1
    b = 1
    while True:
        yield b
        a,b = b, a+b

def search(k, limit = 100000):
    """searches for the first k examples among first limit pairs"""
    hits = []
    for i,(f,p) in enumerate(zip(fib(),primes())):
        if i > limit:
            return "Not found"
        elif f % p == 0:
            hits.append((i,f,p))
            if len(hits) == k: return hits
