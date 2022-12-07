from dataclasses import dataclass, field


@dataclass
class Inventory:
    content: list[int] = field(default_factory=list)

    def total(self):
        return sum(self.content)


def read_inventory(filename: str):
    with open(filename, "r") as f:
        lines = list(map(lambda x: x.replace("\n", ""), f.readlines()))
        buf = []
        inv = []
        for line in lines:
            if len(line) == 0:
                inv.append(Inventory(content=list(map(int, buf.copy()))))
                buf.clear()
            else:
                buf.append(line)
        else:
            inv.append(Inventory(content=list(map(int, buf.copy()))))
        return list(map(lambda x: x.total(), inv))


def part_one(filename: str):
    res = read_inventory(filename)
    return max(res)


def part_two(filename: str):
    inv = read_inventory(filename)
    content = sorted(inv)[-3:]
    return sum(content)


def main():
    print(f"Part one: {part_one('input.txt')}")
    print(f"Part one: {part_two('input.txt')}")


if __name__ == "__main__":
    main()
