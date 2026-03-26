def is_prime(n):
    """Check if a number is prime.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_upto(n):
    """Generate a list of all prime numbers up to and including n.
    
    Args:
        n (int): The upper bound (inclusive) for prime generation.
    
    Returns:
        list[int]: List of prime numbers from 2 to n (if n is prime) or up to the largest prime ≤ n.
    """
    return [i for i in range(2, n + 1) if is_prime(i)]

def main():
    """Read an integer from standard input, compute primes up to that integer, and print the result."""
    n = int(input())
    result = primes_upto(n)
    print(result)

if __name__ == "__main__":
    """Execute the main function when the script is run directly."""
    main()