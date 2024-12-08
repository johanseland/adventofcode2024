from pathlib import Path


def read_input(filename: Path) -> list[tuple[int, list[int]]]:
    puzzle = []

    with open(filename, "r") as file:
        for line in file.readlines():
            input = line.split(":")
            key = int(input[0])

            puzzle.append((key, list(map(int, input[1].split()))))

    return puzzle


def can_value_be_constructed(value: int, numbers: list[int]) -> bool:
    if len(numbers) == 2:
        return numbers[0] + numbers[1] == value or numbers[0] * numbers[1] == value
    else:
        add = numbers[0] + numbers[1]
        mul = numbers[0] * numbers[1]

        return can_value_be_constructed(
            value, [add] + numbers[2:]
        ) or can_value_be_constructed(value, [mul] + numbers[2:])


def can_value_be_constructed2(value: int, numbers: list[int]) -> bool:
    if len(numbers) == 2:
        concat = int(f"{numbers[0]}{numbers[1]}")
        return (
            numbers[0] + numbers[1] == value
            or numbers[0] * numbers[1] == value
            or concat == value
        )
    else:
        add = numbers[0] + numbers[1]
        mul = numbers[0] * numbers[1]
        concat = int(f"{numbers[0]}{numbers[1]}")

        return (
            can_value_be_constructed2(value, [add] + numbers[2:])
            or can_value_be_constructed2(value, [mul] + numbers[2:])
            or can_value_be_constructed2(value, [concat] + numbers[2:])
        )


def compute_total_calibration(puzzle: list[tuple[int, list[int]]]) -> int:
    test_values = [val[0] for val in puzzle if can_value_be_constructed(val[0], val[1])]
    return sum(test_values)


def compute_total_calibration2(puzzle: list[tuple[int, list[int]]]) -> int:
    test_values = [
        val[0] for val in puzzle if can_value_be_constructed2(val[0], val[1])
    ]
    return sum(test_values)


def test_read_input():
    puzzle = read_input(Path("tests/07/example_07.txt"))

    assert puzzle[0] == (190, [10, 19])
    assert puzzle[7] == (21037, [9, 7, 18, 13])
    assert len(puzzle) == 9


def test_can_value_be_construct():
    puzzle = read_input(Path("tests/07/example_07.txt"))

    assert can_value_be_constructed(puzzle[0][0], puzzle[0][1])
    assert can_value_be_constructed(puzzle[1][0], puzzle[1][1])
    assert can_value_be_constructed(puzzle[8][0], puzzle[8][1])


def test_can_value_be_constructed2() -> None:
    assert can_value_be_constructed2(156, [15, 6])
    assert can_value_be_constructed2(7290, [6, 8, 6, 15])
    assert can_value_be_constructed2(192, [17, 8, 14])


def test_compute_total_calibration() -> None:
    puzzle = read_input(Path("tests/07/example_07.txt"))
    assert compute_total_calibration(puzzle) == 3749


def test_compute_total_calibration2() -> None:
    puzzle = read_input(Path("tests/07/example_07.txt"))
    assert compute_total_calibration2(puzzle) == 11387


if __name__ == "__main__":
    input_file = Path(__file__).parent / "07_input.txt"
    puzzle = read_input(input_file)

    total_calibration = compute_total_calibration(puzzle)
    total_calibration2 = compute_total_calibration2(puzzle)

    print(f"Total calibration result: {total_calibration}")
    print(f"Total calibration2 result: {total_calibration2}")
