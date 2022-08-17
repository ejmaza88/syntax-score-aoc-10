from typing import List, Union

# PUZZLE_INPUT = "puzzle_short.txt"
PUZZLE_INPUT = "puzzle.txt"

CHUNK_KEYS = {"(": ")", "[": "]", "{": "}", "<": ">"}
SYNTAX_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
VALID_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}
SCORE_CONSTANT = 5

OPENERS = CHUNK_KEYS.keys()
CLOSERS = CHUNK_KEYS.values()


def process_chunk(chunk: str = None) -> Union[List, str]:
    char_list = []

    for char in chunk:
        if char in OPENERS:
            char_list.append(char)

        elif char in CLOSERS:
            last_char_from_list = char_list[-1]
            closer_char = CHUNK_KEYS.get(last_char_from_list)

            if char == closer_char:
                char_list = char_list[:-1]

            else:
                return char

    return char_list


def calculate_syntax_error_score(invalid_list: List[str] = None) -> int:
    score = 0

    for char in invalid_list:
        score += SYNTAX_POINTS.get(char)

    return score


def autocomplete_score_per_chunk(valid_chunk: List[str] = None) -> int:
    score = 0

    for index, _ in enumerate(valid_chunk, start=1):
        char = valid_chunk[-index]
        closer_char = CHUNK_KEYS.get(char)
        score = (score * SCORE_CONSTANT) + VALID_POINTS.get(closer_char)

    return score


def find_autocomplete_score(score_list: List[int] = None) -> int:
    return sorted(score_list)[int(len(score_list) / 2)]


def syntax_scoring_part_one() -> None:
    invalid = []  # list of invalid chars

    with open(PUZZLE_INPUT, "r") as f:
        for line in f:
            chunk_output = process_chunk(chunk=line.strip())
            if isinstance(chunk_output, str):
                invalid.append(chunk_output)

    error_score = calculate_syntax_error_score(invalid_list=invalid)

    print(error_score)


def syntax_scoring_part_two() -> None:
    score_list = []

    with open(PUZZLE_INPUT, "r") as f:
        for line in f:
            chunk_output = process_chunk(chunk=line.strip())

            if isinstance(chunk_output, list):
                score = autocomplete_score_per_chunk(valid_chunk=chunk_output)
                score_list.append(score)

    autocomplete_score = find_autocomplete_score(score_list=score_list)
    print(autocomplete_score)


if __name__ == "__main__":
    print("-- Part One --")
    syntax_scoring_part_one()
    print()
    print("-- Part Two --")
    syntax_scoring_part_two()


