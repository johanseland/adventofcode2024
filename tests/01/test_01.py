from pathlib import Path
import requests
import sys


def read_input(filename: Path) -> tuple[list[int], list[int]]:
    l0, l1 = [], []

    with open(filename, "r") as file:
        for line in file:
            try:
                x, y = map(int, line.split())
                l0.append(x)
                l1.append(y)
            except ValueError:
                pass

    return l0, l1


def compute_total_distance(l0: list[int], l1: list[int]) -> int:
    l0.sort()
    l1.sort()

    total_distance = 0
    for i in range(len(l0)):
        total_distance += abs(l0[i] - l1[i])

    return total_distance


def compute_similarity_score(l0: list[int], l1: list[int]) -> int:
    counts: dict[int, int] = {}
  
    for i in range(len(l1)):
      counts[l1[i]] = counts.get(l1[i], 0) + 1
    
    similarity_score = 0
    
    for val in l0:
      similarity_score += val * counts.get(val, 0)
      
    return similarity_score

  
def test_read_input() -> None:
    input_file = Path(__file__).parent / "01_example.txt"
    l0, l1 = read_input(input_file)
    assert l0 == [3, 4, 2, 1, 3, 3]
    assert l1 == [4, 3, 5, 3, 9, 3]


def test_total_distance() -> None:
    input_file = Path(__file__).parent / "01_example.txt"
    l0, l1 = read_input(input_file)
    assert compute_total_distance(l0, l1) == 11

def test_similarity_score() -> None:
    input_file = Path(__file__).parent / "01_example.txt"
    l0, l1 = read_input(input_file)
    assert compute_similarity_score(l0, l1) == 31


def main() -> int:
    input_file = Path(__file__).parent / "01_input.txt"
    if not input_file.exists():
        return 1

    l0, l1 = read_input(input_file)
    print(f"Total distace: {compute_total_distance(l0, l1)}")
    print(f"Similarity score: {compute_similarity_score(l0, l1)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
