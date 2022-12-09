from itertools import islice
from typing import Iterable


def get_priority(letter: str):
    code = ord(letter)
    if ord("a") <= code <= ord("z"):
        return code - ord("a") + 1
    elif ord("A") <= code <= ord("Z"):
        return code - ord("A") + 27
    assert False, "Should be unreachable"


def in_both_compartments(first_compartments: str, second_compartments: str) -> str:
    first_set = set(first_compartments)
    second_set = set(second_compartments)
    intersection = first_set.intersection(second_set)
    assert len(intersection) == 1, "Attention, more then 1 element in both compartments"
    assert len(intersection) != 0, "Attention, empty intersection"
    return "".join(intersection)


def split_by_compartments(content: str) -> tuple[str, str]:
    compartment_len = len(content) // 2
    return content[:compartment_len], content[compartment_len:]


def part_one(data: list[str]):
    return sum(
        map(
            get_priority,
            map(
                lambda comps: in_both_compartments(*comps),
                map(split_by_compartments, data),
            ),
        )
    )


def chunk(arr_range: Iterable, arr_size: int):
    arr_range = iter(arr_range)
    return iter(lambda: tuple(islice(arr_range, arr_size)), ())


def common_in_group(
    first_rucksack: str, second_rucksack: str, third_rucksack: str
) -> str:
    first_set = set(first_rucksack)
    second_set = set(second_rucksack)
    third_set = set(third_rucksack)
    intersection = first_set.intersection(second_set).intersection(third_set)
    assert len(intersection) == 1, "Attention, more then 1 element in both compartments"
    assert len(intersection) != 0, "Attention, empty intersection"
    return "".join(intersection)


def part_two(data: list[str]):
    return sum(
        map(get_priority, map(lambda group: common_in_group(*group), chunk(data, 3)))
    )


def read_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def main():
    data = read_data("input.txt")
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")


if __name__ == "__main__":
    main()
