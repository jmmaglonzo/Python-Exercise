def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def generate_primes(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

def main():
    start, end = 1, 250
    primes = generate_primes(start, end)

    with open("results.txt", "w") as file:
        file.write("\n".join(map(str, primes)))

    print("Prime numbers between 1 and 250 are saved in results.txt.")

if __name__ == "__main__":
    main()
