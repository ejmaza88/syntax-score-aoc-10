from typing import List, Union

# PUZZLE_INPUT = "puzzle_short.txt"
PUZZLE_INPUT = "puzzle.txt"

CHUNK_KEYS = {"(": ")", "[": "]", "{": "}", "<": ">"}
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}

openers = CHUNK_KEYS.keys()
closers = CHUNK_KEYS.values()


def illegal_chunk(chunk: str = None, invalid_list: List[str] = None) -> None:
    char_list = []

    for char in chunk:
        if char in openers:
            char_list.append(char)

        elif char in closers:
            last_char_from_list = char_list[-1]
            closer_char = CHUNK_KEYS.get(last_char_from_list)

            if char == closer_char:
                char_list = char_list[:-1]

            else:
                invalid_list.append(char)
                return


def syntax_error_score(invalid_list: List[str] = None) -> int:
    score = 0
    for char in invalid_list:
        score += POINTS.get(char)

    return score


if __name__ == "__main__":
    invalid = []  # list of invalid chars

    with open(PUZZLE_INPUT, "r") as f:
        for line in f:
            illegal_chunk(chunk=line.strip(), invalid_list=invalid)

    error_score = syntax_error_score(invalid_list=invalid)

    # print(invalid)
    print(error_score)


