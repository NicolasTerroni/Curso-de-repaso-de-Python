def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
    return True

def run():
    pass

    number = int(input("Input your number: "))

    result = is_prime(number)

    if result:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} isn't a prime number.")


if __name__ == "__main__":
    run()