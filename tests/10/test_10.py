from pathlib import Path


def read_input(path: Path) -> list[list[int]]:
    input: list[list[int]] = []

    with open(path) as file:
        for line in file:
            input.append([int(c) for c in line.strip()])

    return input


def score_trailhead(
    row: int, col: int, map: list[list[int]], is_used: list[list[int]]
) -> int:
    def in_range(row: int, col: int) -> bool:
        return 0 <= row < len(map) and 0 <= col < len(map[0])

    if is_used[row][col] > 0:
        return 0

    is_used[row][col] = 1
    curr = map[row][col]

    if curr == 9:
        return 1

    score = 0

    for r in [-1, 1]:
        if in_range(row + r, col) and map[row + r][col] == curr + 1:
            score += score_trailhead(row + r, col, map, is_used)

    for c in [-1, 1]:
        if in_range(row, col + c) and map[row][col + c] == curr + 1:
            score += score_trailhead(row, col + c, map, is_used)

    return score


def rate_trailhead(row: int, col: int, map: list[list[int]]) -> int:
    def in_range(row: int, col: int) -> bool:
        return 0 <= row < len(map) and 0 <= col < len(map[0])

    curr = map[row][col]

    if curr == 9:
        return 1

    rating = 0

    for r in [-1, 1]:
        if in_range(row + r, col) and map[row + r][col] == curr + 1:
            rating += rate_trailhead(row + r, col, map)

    for c in [-1, 1]:
        if in_range(row, col + c) and map[row][col + c] == curr + 1:
            rating += rate_trailhead(row, col + c, map)

    return rating


def sum_trailheads(map: list[list[int]]) -> int:
    sum = 0

    rows = len(map)
    cols = len(map[0])

    for row in range(rows):
        for col in range(cols):
            if map[row][col] == 0:
                is_used = [[0 for _ in range(cols)] for _ in range(rows)]
                sum += score_trailhead(row, col, map, is_used)

    return sum


def sum_trailhead_ratings(map: list[list[int]]) -> int:
    sum = 0

    rows = len(map)
    cols = len(map[0])

    for row in range(rows):
        for col in range(cols):
            if map[row][col] == 0:
                sum += rate_trailhead(row, col, map)

    return sum


def test_read_input() -> None:
    map = read_input(Path("tests/10/example_10.txt"))

    assert len(map) == 8
    assert map[0] == [8, 9, 0, 1, 0, 1, 2, 3]


def test_sum_trailheads() -> None:
    map = read_input(Path("tests/10/example_10.txt"))

    assert sum_trailheads(map) == 36


def test_rate_trailheads() -> None:
    map = read_input(Path("tests/10/example_10.txt"))

    assert sum_trailhead_ratings(map) == 81


if __name__ == "__main__":
    map = read_input(Path("tests/10/10_input.txt"))
    assert len(map) == 47

    sum = sum_trailheads(map)
    rate = sum_trailhead_ratings(map)
    print(f"Sum of all trailheads: {sum}")
    print(f"Sum of all trailhead ratings: {rate}")
