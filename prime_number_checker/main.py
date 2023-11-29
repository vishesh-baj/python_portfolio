n = int(input("Check this number t obe prime or not: "))


def check_is_prime(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime number")
            isPrime = False
        else:
            isPrime = True


check_is_prime(13)