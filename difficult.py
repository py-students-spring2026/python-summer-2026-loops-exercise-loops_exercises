def one(number):
    """
    Write a program that finds the prime factors of a given number using a for loop. A prime factor is a prime number that divides another number exactly without leaving a remainder, e.g. the prime factors of 12 are 2 and 3.
    """
    print("\ndifficult.one:")

    def is_prime(number):
        """
        Determines whether a given number is prime.
        @param number The number to check.
        @return True if prime, false otherwise.
        """
        is_prime = True # assume it's prime
        divisor = number - 1
        while divisor > 1:
            if number % divisor == 0:
                is_prime = False
                break
            divisor -= 1
        return is_prime
    
    print('\t', f'The prime factors of {number} are: ', end='')
    for divisor in range(number-1, 1, -1):
        if (number % divisor) == 0:
            if is_prime(divisor):
                print(f'{divisor}, ', end='')
    print() # line break


def two():
    """
    Write a program that calculates the nth term of the Fibonacci sequence using a while loop.
    """
    print("\ndifficult.two:")
    pass

def three():
    """
    Write a program that checks if a given string is an anagram using a for loop.
    """
    print("\ndifficult.three:")

    pass

def four():
    """
    Write a program that prints the first n terms of the arithmetic sequence using a while loop. An arithmetic sequence is a sequence of numbers in which each term after the first is found by adding a fixed, non-zero number called the common difference to the previous term, e.g. 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, ..., where the common difference is 2.
    """
    print("\ndifficult.four:")

    pass

def five():
    """
    Write a program that finds the median of a given list of numbers using a for loop. The median is the middle value of a list of numbers when they are sorted in ascending order. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.
    """
    print('\ndifficult.five:')

    pass

def six():
    """
    Write a program that checks if a given number is a perfect number using a while loop. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself, e.g. 6 is a perfect number because 1 + 2 + 3 = 6.
    """
    print('\ndifficult.six:')

    pass

def seven():
    """
    Write a program that prints the sum of all digits in a given number using a for loop. For example, the sum of the digits in 12345 is 1 + 2 + 3 + 4 + 5 = 15.
    """
    print('\ndifficult.seven:')

    pass

def eight():
    """
    Write a program that finds the longest word in a given sentence using a while loop.
    """
    print('\ndifficult.eight:')

    pass
        
def nine():
    """
    Write a program that checks if a given string is a pangram using a for loop. A pangram is a sentence that contains every letter of the alphabet at least once, e.g. The quick brown fox jumps over the lazy dog.
    """
    print('\ndifficult.nine:')

    pass

def ten():
    """
    Write a program that prints the prime numbers between 1 and 1000 using a while loop.
    """
    print('\ndifficult.ten:')

    pass

