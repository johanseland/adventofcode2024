import concurrent.futures
import time
import itertools


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


def apply_rules_multiprocess(input: list[int], chunk_size: int) -> list[int]:
    def chunked_iterable(iterable, size):
        it = iter(iterable)
        while True:
            chunk = list(itertools.islice(it, size))
            if not chunk:
                break
            yield chunk

    subsets = chunked_iterable(input, chunk_size)

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        # future = executor.submit(pow, 323, 1235)
        future = list(executor.map(apply_rules, subsets))

    return [item for sublist in future for item in sublist]


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


def test_apply_rules_threading() -> None:
    prev = [6571, 0, 5851763, 526746, 23, 69822, 9, 989]

    chunk_size = 10000
    for i in range(30):
        if len(prev) < chunk_size:
            next = apply_rules(prev)
        else:
            next = apply_rules_multiprocess(prev, chunk_size)

        prev = next
        # print(f"Num blinks: {i} - number of stones: {len(next)}")


if __name__ == "__main__":
    input = [6571, 0, 5851763, 526746, 23, 69822, 9, 989]

    blinks = 35

    prev = input
    for i in range(blinks):
        start = time.perf_counter()
        next = apply_rules(prev)
        prev = next
        end = time.perf_counter() - start
        print(f"Num blinks: {i} - number of stones: {len(next)}, time: {end}s")

    # blinks = 40
    prev = input
    chunk_size = 100000
    for i in range(blinks):
        start = time.perf_counter()

        if len(prev) < chunk_size:
            next = apply_rules(prev)
        else:
            next = apply_rules_multiprocess(prev, chunk_size)

        prev = next
        # Code you want to time
        end = time.perf_counter() - start
        print(
            f"Num blinks (multiprocess): {i} - number of stones: {len(next)}, time: {end}s"
        )

    print(f"Number of stones after {blinks} blinks: {len(next)}")
