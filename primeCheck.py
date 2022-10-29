from doctest import testmod
import sys
import decimal


def factors(A: list, x: int) -> None:
    print('%i = ' % x, end="")
    k, i = 0, 0
    while i < len(A):
        n = A.count(A[i])
        if n == 1:
            print(f'{A[i]:,}', end="")
            k += 1
            i += 1
        else:
            print('{}^{}'.format(f'{A[i]}', n), end="")
            s = A[i]
            while s in A:
                A.remove(s)
        if k < len(A):
            print(' * ', end="")
    print()


def all_prime_factors(p: int) -> list:
    number = p
    allFactors = []
    loop = 2
    while loop * loop <= p:
        if p % loop:
            loop += 1
        else:
            p //= loop
            allFactors.append(loop)
            
    if p > 1:
        allFactors.append(p)
    allFactors.sort()
    factors(allFactors, number)


def is_prime(pp: int) -> bool:
    if pp == 2 or pp == 3:
        return True
    elif pp < 2 or not pp % 2:
        return False

    odd_n = range(3, int(decimal.Decimal(pp).sqrt() + 1), 2)
    return not any(not pp % i for i in odd_n)


def prime_check(x: int) -> bool:
    if is_prime(x):
        return True
    else:
        all_prime_factors(x)


def test_prime_check():
    """
    >>> prime_check(0)
    0 = 
    >>> prime_check(1)
    1 = 
    >>> prime_check(7)
    True
    >>> prime_check(496)
    496 = 2^4 * 31
    >>> prime_check(30030)
    30030 = 2 * 3 * 5 * 7 * 11 * 13
    >>> prime_check(5450195689)
    True
    >>> prime_check(-20)
    -20 = 
    """
    pass


if __name__ == "__main__":
    if(sys.argv[1:]):
        prime_check(int(sys.argv[1]))
    else:
        testmod()