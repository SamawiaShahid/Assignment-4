def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    name = input("Enter your name: ")
    numbers = []
    for i in range(1, 4):
        while True:
            try:
                number = int(input(f"Enter your {i} favorite number: "))
                numbers.append(number)
                break
            except ValueError:
                print("Please enter a valid integer.")
    print(f"\nHello, {name}! Let's explore your favorite numbers:")

    even_odd_info = []
    for number in numbers:
        if number % 2 == 0:
            even_odd_info.append((number, "even"))
        else:
            even_odd_info.append((number, "odd"))

    for number, status in even_odd_info:
        print(f"The number {number} is {status}.")
    print("\nHere are your numbers and their squares:")
    for number in numbers:
        print(f"The number {number} and its square: ({number}, {number ** 2})")
    
    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number, but it's still interesting!")

if __name__ == "__main__":
    main()
