def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_upto(n):
    return [i for i in range(2, n + 1) if is_prime(i)]

def main():
    n = int(input())
    result = primes_upto(n)
    print(result)

if __name__ == "__main__":
    main()
