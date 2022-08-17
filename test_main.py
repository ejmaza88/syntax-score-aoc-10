import unittest

from main import (
    process_chunk,
    calculate_syntax_error_score,
    autocomplete_score_per_chunk,
    find_autocomplete_score,
)


class TestSyntaxScoring(unittest.TestCase):

    def test_process_chunk(self):
        data = [
            # invalid chunks
            ("}", "{([(<{}[<>[]}>{[]{[(<()>"),
            (")", "[[<[([]))<([[{}[[()]]]"),

            # incomplete chunks
            (["[", "(", "{", "(", "[", "[", "{", "{"], "[({(<(())[]>[[{[]{<()<>>"),
            (["(", "{", "[", "<", "{", "("], "[(()[<>])]({[<{<<[]>>("),
        ]

        for chunk in data:
            expected_output = chunk[0]
            actual_chunk_output = process_chunk(chunk[1])

            self.assertEqual(actual_chunk_output, expected_output)

    def test_calculate_syntax_error_score(self):
        expected_score = 26397
        actual_score = calculate_syntax_error_score([x for x in "))]}>"])

        self.assertEqual(actual_score, expected_score)

    def test_autocomplete_score_per_chunk(self):
        expected_score = 288957
        actual_score = autocomplete_score_per_chunk([x for x in "[({([[{{"])

        self.assertEqual(actual_score, expected_score)

    def test_find_autocomplete_score(self):
        expected_score = 100
        actual_score = find_autocomplete_score([100, 200, 80, 1, 300])

        self.assertEqual(actual_score, expected_score)


if __name__ == '__main__':
    unittest.main()
