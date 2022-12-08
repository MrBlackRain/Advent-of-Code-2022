from __future__ import annotations

from enum import Enum, IntEnum


class Shape(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

    @staticmethod
    def lose_to(other: Shape):
        lose_dict = {
            Shape.ROCK: Shape.PAPER,
            Shape.PAPER: Shape.SCISSORS,
            Shape.SCISSORS: Shape.ROCK,
        }
        return lose_dict[other]

    @staticmethod
    def wins(other: Shape):
        win_dict = {
            Shape.ROCK: Shape.SCISSORS,
            Shape.PAPER: Shape.ROCK,
            Shape.SCISSORS: Shape.PAPER,
        }
        return win_dict[other]

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __gt__(self, o: object) -> bool:
        if self == Shape.ROCK:
            return o == Shape.SCISSORS
        elif self == Shape.PAPER:
            return o == Shape.ROCK
        return o == Shape.PAPER

    def __lt__(self, o: object) -> bool:
        if self == Shape.ROCK:
            return o == Shape.PAPER
        elif self == Shape.PAPER:
            return o == Shape.SCISSORS
        return o == Shape.ROCK

    def __hash__(self):
        return hash(self.value)


class GameResult(IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6


def symbol_to_shape(val: str):
    match_d = {
        "X": Shape.ROCK,
        "A": Shape.ROCK,
        "Y": Shape.PAPER,
        "B": Shape.PAPER,
        "Z": Shape.SCISSORS,
        "C": Shape.SCISSORS,
    }
    return match_d[val]


def calc_score(your_shape: Shape, result: GameResult):
    points = {Shape.ROCK: 1, Shape.PAPER: 2, Shape.SCISSORS: 3}
    return result.value + points[your_shape]


def evaluate_game_result(hands: tuple[Shape, Shape]) -> GameResult:
    opponent, you = hands
    if you > opponent:
        return GameResult.WIN
    elif you < opponent:
        return GameResult.LOSS
    return GameResult.DRAW


def letter_to_game_result(letter: str) -> GameResult:
    gr_l = {"X": GameResult.LOSS, "Y": GameResult.DRAW, "Z": GameResult.WIN}
    return gr_l[letter]


def deduce_shape(opponents_hand: Shape, expected_result: GameResult) -> Shape:
    if expected_result == GameResult.DRAW:
        return opponents_hand
    elif expected_result == GameResult.LOSS:
        return Shape.wins(opponents_hand)
    return Shape.lose_to(opponents_hand)


def part_one(data: list[str]):
    return sum(
        map(
            lambda k: calc_score(k[0], k[1]),
            map(
                lambda shapes: (
                    shapes[1],
                    evaluate_game_result(shapes),
                ),
                map(
                    lambda x: tuple(x),
                    map(
                        lambda pair: map(symbol_to_shape, pair),
                        map(lambda s: s.split(" "), data),
                    ),
                ),
            ),
        )
    )


def part_two(data: list[str]):
    return sum(
        map(
            lambda x: calc_score(x[0], x[1]),
            map(
                lambda d: (deduce_shape(d[0], d[1]), d[1]),
                map(
                    lambda hint: (
                        symbol_to_shape(hint[0]),
                        letter_to_game_result(hint[1]),
                    ),
                    map(lambda s: s.split(" "), data),
                ),
            ),
        )
    )


def read_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def main():
    data = read_data("input_test.txt")
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")


if __name__ == "__main__":
    main()
