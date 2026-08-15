def calculate_stats(numbers: list[float]) -> dict:
    """Return total, average, max, and min for a list of numbers."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    total = sum(numbers)
    avg = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return {"total": total, "average": avg, "max": maximum, "min": minimum}


def find_duplicates(items: list) -> list:
    """Return the list of values that appear more than once in items, in order of first repeat."""
    seen = set()
    duplicates = []

    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)

    return duplicates


if __name__ == "__main__":
    data = [4, 2, 7, 2, 9, 4, 1]
    print(calculate_stats(data))
    print(find_duplicates(data))
