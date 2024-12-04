from pathlib import Path
import sys
from typing import Optional


def read_input(filename: Path) -> list[str]:
    puzzle = []

    with open(filename, "r") as file:
        puzzle = file.read().splitlines()

    return puzzle


def count_occurrences(word: str, puzzle: list[str]) -> int:
    def check_word(w: str, r: int, c: int, direction: tuple[int, int]) -> bool:
        if len(w) == 0:
            return True

        if r < 0 or r >= len(puzzle) or c < 0 or c >= len(puzzle[r]):
            return False

        if puzzle[r][c] != w[0]:
            return False

        return check_word(w[1:], r + direction[0], c + direction[1], direction)

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    occurrences = 0
    for r in range(len(puzzle)):
        for c in range(len(puzzle[r])):
            for direction in directions:
                if check_word(word, r, c, direction):
                    occurrences += 1

    return occurrences


def count_x_mas(puzzle: list[str]) -> int:
    def diag3_right(r: int, c: int) -> Optional[str]:
        if r < 1 or r >= len(puzzle) - 1 or c < 1 or c >= len(puzzle[r]) - 1:
            return None

        return puzzle[r - 1][c - 1] + puzzle[r][c] + puzzle[r + 1][c + 1]

    def diag3_left(r: int, c: int) -> Optional[str]:
        if r < 1 or r >= len(puzzle) - 1 or c < 1 or c >= len(puzzle[r]) - 1:
            return None

        return puzzle[r + 1][c - 1] + puzzle[r][c] + puzzle[r - 1][c + 1]

    valid_diags = ["MAS", "SAM"]
    count = 0

    for r in range(len(puzzle)):
        for c in range(len(puzzle[r])):
            if puzzle[r][c] == "A":
                right = diag3_right(r, c)
                left = diag3_left(r, c)

                if right and left and right in valid_diags and left in valid_diags:
                    count += 1

    return count


def test_read_input() -> None:
    input_file = Path(__file__).parent / "04_example.txt"
    puzzle = read_input(input_file)

    assert puzzle[0] == "MMMSXXMASM"


def test_count_occurences() -> None:
    input_file = Path(__file__).parent / "04_example.txt"
    puzzle = read_input(input_file)
    assert count_occurrences("XMAS", puzzle) == 18


def test_count_x_mas() -> None:
    input_file = Path(__file__).parent / "04_example.txt"
    puzzle = read_input(input_file)
    assert count_x_mas(puzzle) == 9


def main() -> None:
    input_file = Path(__file__).parent / "04_input.txt"
    puzzle = read_input(input_file)

    print(count_occurrences("XMAS", puzzle))
    print(count_x_mas(puzzle))


if __name__ == "__main__":
    main()
