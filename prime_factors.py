import math
def main():
    number = int(input("Enter a number: "))
    prime_factors = find_prime_factors_2(number)
    print(prime_factors)


def find_prime_factors(number):
    prime_factors = []
    if number < 2:
        return prime_factors
    P = 2
    while number > 1:
        while number % P == 0:
            prime_factors.append(P)
            number /= P
        P += 1
    return prime_factors


def find_prime_factors_2(number):
    prime_factors = []
    if number < 2:
        return prime_factors
    for P in range(2, round(math.sqrt(number)+1)):
        while number % P == 0:
            prime_factors.append(P)
            number /= P
            if number < 2:
                return prime_factors
    if number > 1:
        prime_factors.append(number)
        return prime_factors






if __name__ == "__main__":
    main()