# Generate a continous number given a prefix,
# the start of the number, and the end of the number.
# Return a list of the generated numbers.
def generate_number(prefix, number):
    return f"{prefix}{number}"


def generate_numbers(prefix: str, start: int, end: int):
    return [generate_number(prefix, i) for i in range(start, end + 1)]


# Write list of numbers to a file
def write_to_file(numbers: str, filename: str):
    with open(filename, "w") as f:
        f.write("\n".join(numbers))


def main():
    prefix = "MZ"
    start = 923987
    end = 926690
    numbers = generate_numbers(prefix, start, end)
    write_to_file(numbers, "numbers.txt")


if __name__ == "__main__":
    main()
