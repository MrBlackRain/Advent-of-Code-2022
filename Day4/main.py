from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SectionRange:
    left_boundary: int
    right_boundary: int

    def fully_contains(self, other: SectionRange) -> bool:
        return (
            self.left_boundary >= other.left_boundary
            and self.right_boundary <= other.right_boundary
        )

    def overlaps(self, other: SectionRange) -> bool:
        return (
            other.left_boundary <= self.left_boundary <= other.right_boundary
            or other.left_boundary <= self.right_boundary <= other.right_boundary
        )


def split_pairs(pairs: str) -> tuple[SectionRange, SectionRange]:
    return tuple(map(lambda p: SectionRange(*map(int, p.split("-"))), pairs.split(",")))


def is_section_ranges_fully_overlaps(first: SectionRange, second: SectionRange) -> bool:
    return first.fully_contains(second) or second.fully_contains(first)


def part_one(data: list[str]):
    return len(
        list(
            filter(
                lambda is_overlap: is_overlap,
                map(
                    lambda range_pair: is_section_ranges_fully_overlaps(*range_pair),
                    map(lambda pairs: split_pairs(pairs), data),
                ),
            )
        )
    )


def any_overlap(first_range: SectionRange, second_range: SectionRange) -> bool:
    return first_range.overlaps(second_range) or second_range.overlaps(first_range)


def part_two(data: list[str]):
    return len(
        list(
            filter(
                lambda is_overlap: is_overlap,
                map(
                    lambda range_pair: any_overlap(*range_pair),
                    map(lambda pairs: split_pairs(pairs), data),
                ),
            )
        )
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
