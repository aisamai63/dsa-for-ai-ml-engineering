"""Basic examples of common Big O time complexities."""


def get_first(numbers: list[int]) -> int:
    """Return the first item.

    Time complexity: O(1)
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")

    return numbers[0]


def get_last(numbers: list[int]) -> int:
    """Return the last item.

    Time complexity: O(1)
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")

    return numbers[-1]


def print_all(numbers: list[int]) -> None:
    """Print every item.

    Time complexity: O(n)
    """
    for number in numbers:
        print(number)


def calculate_total(numbers: list[int]) -> int:
    """Calculate the sum of all items.

    Time complexity: O(n)
    """
    total = 0

    for number in numbers:
        total += number

    return total


def contains_value(numbers: list[int], target: int) -> bool:
    """Check whether the target exists.

    Worst-case time complexity: O(n)
    """
    for number in numbers:
        if number == target:
            return True

    return False


def main() -> None:
    numbers = [10, 20, 30, 40, 50]

    print("First:", get_first(numbers))
    print("Last:", get_last(numbers))
    print("Total:", calculate_total(numbers))
    print("Contains 30:", contains_value(numbers, 30))

    print("\nAll values:")
    print_all(numbers)


if __name__ == "__main__":
    main()
