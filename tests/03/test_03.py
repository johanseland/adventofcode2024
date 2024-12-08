import re
from itertools import cycle


def sum_valid_muls(input: str) -> int:
    p = re.compile("mul\((\d+),(\d+)\)")
    sum = 0
    for mul in p.finditer(input):
        sum += int(mul[1]) * int(mul[2])

    return sum


def sum_enabled_muls(input: str) -> int:
    # Order is important, this implies the starting instruction is do(),
    tokens = ["don't()", "do()"]

    cycler = cycle(tokens)
    token = next(cycler)

    start, sum = 0, 0

    while start != len(input):
        end = input.find(token, start)
        # Read to end of input if we cannot find more tokens.
        if end == -1:
            end = len(input)

        # Implies the current instruction is do().
        if token == "don't()":
            s = input[start:end]
            sum += sum_valid_muls(s)
        start = end
        token = next(cycler)

    return sum


def test_sum_valid_muls() -> None:
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    assert sum_valid_muls(input) == 161


def test_sum_enabled_muls() -> None:
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    assert sum_enabled_muls(input) == 48


if __name__ == "__main__":
    with open("tests/03/03_input.txt") as file:
        input = file.read()

    valid_sum = sum_valid_muls(input)
    enabled_sum = sum_enabled_muls(input)

    print(f"Sum of valid muls: {valid_sum}")
    print(f"Sum of enabled muls: {enabled_sum}")
