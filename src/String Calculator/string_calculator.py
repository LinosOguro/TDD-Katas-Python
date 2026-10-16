def add(numbers):
    if numbers == "":
        return 0

    values = [int(value) for value in numbers.replace("\n", ",").split(",")]
    negatives = [value for value in values if value < 0]

    if negatives:
        raise ValueError(
            "negative numbers not allowed: "
            + ", ".join(str(value) for value in negatives)
        )

    return sum(values)
