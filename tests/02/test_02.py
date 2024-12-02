from pathlib import Path
import sys


def read_input(filename: Path) -> list[list[int]]:
    reports = []

    with open(filename, "r") as file:
        for line in file:
            try:
                reports.append(list(map(int, line.split())))
            except ValueError:
                pass

    return reports


def is_safe(level: list[int]) -> bool:
    diff = level[0] - level[1]

    if abs(diff) > 3 or diff == 0:
        return False

    is_increasing = diff < 0

    for i in range(1, len(level)):
        diff = abs(level[i] - level[i - 1])
        if diff > 3 or diff == 0:
            return False

        if (is_increasing and level[i] < level[i - 1]) or (
            not is_increasing and level[i] > level[i - 1]
        ):
            return False

    return True


def is_safe_dampen(report: list[int]) -> bool:
    if not is_safe(report):
        for i in range(0, len(report)):
            new_report = report[:i] + report[i + 1 :]
            if is_safe(new_report):
                return True
        return False
    else:
        return True


def test_read_input() -> None:
    input_file = Path(__file__).parent / "02_example.txt"
    reports = read_input(input_file)

    assert reports[0] == [7, 6, 4, 2, 1]
    assert reports[1] == [1, 2, 7, 8, 9]


def test_is_safe() -> None:
    input_file = Path(__file__).parent / "02_example.txt"
    reports = read_input(input_file)

    assert is_safe(reports[0])
    assert not is_safe(reports[1])
    assert not is_safe(reports[2])
    assert not is_safe(reports[3])
    assert not is_safe(reports[4])
    assert is_safe(reports[5])


def test_is_safe_dampener() -> None:
    input_file = Path(__file__).parent / "02_example.txt"
    reports = read_input(input_file)

    assert is_safe_dampen(reports[0])
    assert not is_safe_dampen(reports[1])
    assert not is_safe_dampen(reports[2])
    assert is_safe_dampen(reports[3])
    assert is_safe_dampen(reports[4])
    assert is_safe_dampen(reports[5])

    assert is_safe_dampen([61, 60, 62, 64, 65, 66, 69])


def main() -> int:
    input_file = Path(__file__).parent / "02_input.txt"
    if not input_file.exists():
        return 1

    reports = read_input(input_file)
    count = sum(1 for report in reports if is_safe(report))
    count_dampened = sum(1 for report in reports if is_safe_dampen(report))
    print(f"Safe reports: {count}")
    print(f"Safe reports with dampener: {count_dampened}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
