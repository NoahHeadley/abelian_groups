# Given n, calculate all possible abelian groups of order n
# Author: Noah Headley


def generate_primes(n):  # generates primes up to n using the Sieve of Eratosthenes
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        if (prime[p]):
            for i in range(p*p, n+1, p):
                prime[i] = False
        p = p+1

    sol = []
    for p in range(2, n+1):
        if prime[p]:
            sol.append(p)

    return sol


# Given n returns all prime factors as a set of tuples e.g. 660 = (2,2)(3,1)(5,1)(11,1)
def prime_factors(n, primes):
    temp = n
    factors = []
    for p in primes:
        count = 0
        while(temp % p == 0):
            temp = temp / p
            count = count + 1
        if count > 0:
            factors.append((p, count))
    return factors


def find_all_sums(target, curr, start, out, result):
    if (curr == target):
        out.append(result)

    for i in range(start, target):
        temp = curr + i
        if temp <= target:
            result.append(i)
            find_all_sums(target, temp, i, out, result)
            result.pop()
        else:
            return
    if curr == 0 and start == 1:
        return out


if __name__ == '__main__':
    n = int(input("n = "))
    primes = generate_primes(n)
    print(prime_factors(n, primes))
    factors = prime_factors(n, primes)

    sol = 1
    for (p, exp) in factors:
        sol = sol * (len(find_all_sums(exp, 0, 1, [], [])) + 1)

    print(sol)
