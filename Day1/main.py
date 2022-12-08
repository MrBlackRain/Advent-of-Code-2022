from dataclasses import dataclass, field
from itertools import zip_longest


@dataclass
class Inventory:
    content: list[int] = field(default_factory=list)

    def total(self):
        return sum(self.content)


def split_array(value: str, array: list[str]):
    indices = [i for i, x in enumerate(array) if x == value]
    return list(
        map(
            lambda lr: array[lr[0] : lr[1]],
            zip_longest([0] + list(map(lambda x: x + 1, indices)), indices),
        )
    )


def read_inventory_calories(lines: list[str]) -> list[int]:
    return list(
        map(
            lambda x: x.total(),
            map(lambda c: Inventory(list(map(int, c))), split_array("", lines)),
        )
    )


def part_one(data: list[int]):
    return max(data)


def part_two(data: list[int]):
    return sum(sorted(data)[-3:])


def read_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def main():
    data = read_inventory_calories(read_data("input_test.txt"))
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")


if __name__ == "__main__":
    main()
