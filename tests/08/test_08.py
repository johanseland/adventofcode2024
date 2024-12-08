from pathlib import Path
from collections import defaultdict


def read_input(path: Path) -> tuple[dict[str, list[tuple[int, int]]], tuple[int, int]]:
    d: dict[str, list[tuple[int, int]]] = defaultdict(list)

    with open(path) as file:
        for row, line in enumerate(file):
            for column, char in enumerate(line.strip()):
                if char != ".":
                    d[char].append((row, column))

    return (d, (row + 1, column + 1))


def find_antinodes(
    antennas: list[tuple[int, int]], dims: tuple[int, int]
) -> list[tuple[int, int]]:
    antinodes: list[tuple[int, int]] = []

    def in_range(t: tuple[int, int]):
        return 0 <= t[0] < dims[0] and 0 <= t[1] < dims[1]

    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            a0, a1 = antennas[i], antennas[j]

            dist = (a1[0] - a0[0], a1[1] - a0[1])

            if in_range(an0 := (a0[0] - dist[0], a0[1] - dist[1])):
                antinodes.append(an0)

            if in_range(an1 := (a1[0] + dist[0], a1[1] + dist[1])):
                antinodes.append(an1)

    return antinodes


def find_antinodes2(
    antennas: list[tuple[int, int]], dims: tuple[int, int]
) -> list[tuple[int, int]]:
    antinodes: list[tuple[int, int]] = []

    def in_range(t: tuple[int, int]) -> bool:
        return 0 <= t[0] < dims[0] and 0 <= t[1] < dims[1]

    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            a0, a1 = antennas[i], antennas[j]

            dist = (a1[0] - a0[0], a1[1] - a0[1])

            a = 0
            while in_range(an0 := (a0[0] - a * dist[0], a0[1] - a * dist[1])):
                antinodes.append(an0)
                a += 1

            a = 0
            while in_range(an1 := (a1[0] + a * dist[0], a1[1] + a * dist[1])):
                antinodes.append(an1)
                a += 1

    return antinodes


def count_antinodes(
    antennas_all_frequencies: dict[str, list[tuple[int, int]]], dims: tuple[int, int]
) -> int:
    # Using a set here will remove duplicates from different frequencies.
    antinodes_all_frequencies: set[tuple[int, int]] = set()

    for _, frequency_antennas in antennas_all_frequencies.items():
        antinodes = find_antinodes(frequency_antennas, dims)
        antinodes_all_frequencies.update(antinodes)

    return len(antinodes_all_frequencies)


def count_antinodes2(
    antennas: dict[str, list[tuple[int, int]]], dims: tuple[int, int]
) -> int:
    s: set[tuple[int, int]] = set()

    for _, frequency_antennas in antennas.items():
        antinodes = find_antinodes2(frequency_antennas, dims)
        s.update(antinodes)

    return len(s)


def test_read_input() -> None:
    (input, dims) = read_input(Path("tests/08/example_08.txt"))

    assert (1, 8) in input["0"]
    assert dims == (12, 12)


def test_count_antinodes() -> None:
    (input, dims) = read_input(Path("tests/08/example_08.txt"))

    assert count_antinodes(input, dims) == 14


def test_count_antinodes2() -> None:
    (input, dims) = read_input(Path("tests/08/example_08.txt"))

    assert count_antinodes2(input, dims) == 34


if __name__ == "__main__":
    input, dims = read_input(Path("tests/08/08_input.txt"))
    num_antinodes = count_antinodes(input, dims)
    num_antinodes2 = count_antinodes2(input, dims)
    print(f"Number of antinodes: {num_antinodes}")
    print(f"Number of antinodes with new model: {num_antinodes2}")
