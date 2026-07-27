# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
# =============================================================================

def print_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i:<2} = {number * i}")


def print_tables_up_to_n(n):
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    for number in range(1, n + 1):
        print_multiplication_table(number)
        print("-" * 27)


def main():
    number = int(input("Enter a number: "))
    print()
    print_multiplication_table(number)

    print()
    n = int(input("Enter N (for tables from 1 to N): "))
    print()
    print_tables_up_to_n(n)


if __name__ == "__main__":
    main()