import concurrent.futures
import time
import itertools
from functools import cache


def apply_rules(input: list[int]) -> list[int]:
    output: list[int] = []

    for stone in input:
        if stone == 0:
            output.append(1)
        else:
            ss = str(stone)
            if len(ss) % 2 == 0:
                mid = len(ss) // 2
                s0 = int(ss[:mid])
                s1 = int(ss[mid:])
                output.extend([s0, s1])
            else:
                output.append(stone * 2024)

    return output


@cache
def count_depth_first(val: int, steps_to_go: int) -> int:
    if steps_to_go == 0:
        return 1

    if val == 0:
        return count_depth_first(1, steps_to_go - 1)
    else:
        ss = str(val)
        if len(ss) % 2 == 0:
            mid = len(ss) // 2
            s0 = int(ss[:mid])
            s1 = int(ss[mid:])
            return count_depth_first(s0, steps_to_go - 1) + count_depth_first(
                s1, steps_to_go - 1
            )
        else:
            return count_depth_first(val * 2024, steps_to_go - 1)


def count_stones(input: list[int], depth: int) -> int:
    sum = 0
    for i in input:
        sum += count_depth_first(i, depth)

    return sum


def test_count_stones() -> None:
    input = [125, 17]
    assert count_stones(input, 0) == 2
    assert count_stones(input, 1) == 3
    assert count_stones(input, 2) == 4
    assert count_stones(input, 3) == 5
    assert count_stones(input, 4) == 9
    assert count_stones(input, 25) == 55312


def test_apply_rules() -> None:
    e = [
        [125, 17],
        [253000, 1, 7],
        [253, 0, 2024, 14168],
        [512072, 1, 20, 24, 28676032],
        [512, 72, 2024, 2, 0, 2, 4, 2867, 6032],
        [1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32],
        [
            2097446912,
            14168,
            4048,
            2,
            0,
            2,
            4,
            40,
            48,
            2024,
            40,
            48,
            80,
            96,
            2,
            8,
            6,
            7,
            6,
            0,
            3,
            2,
        ],
    ]
    assert apply_rules(e[0]) == e[1]
    assert apply_rules(e[1]) == e[2]
    assert apply_rules(e[2]) == e[3]
    assert apply_rules(e[3]) == e[4]
    assert apply_rules(e[4]) == e[5]
    assert apply_rules(e[5]) == e[6]

    prev = e[0]
    for i in range(25):
        next = apply_rules(prev)
        prev = next

    assert len(next) == 55312


if __name__ == "__main__":
    input = [6571, 0, 5851763, 526746, 23, 69822, 9, 989]

    blinks = 25

    prev = input
    for i in range(blinks):
        start = time.perf_counter()
        next = apply_rules(prev)
        prev = next
        end = time.perf_counter() - start
        print(f"Num blinks: {i} - number of stones: {len(next)}, time: {end}s")

    print(f"Number of stones after {blinks} blinks: {len(next)}")

    blinks = 75
    start = time.perf_counter()
    stone_count = count_stones(input, blinks)
    end = time.perf_counter() - start
    print(f"Num blinks: {blinks} - number of stones: {stone_count}, time: {end}s")
