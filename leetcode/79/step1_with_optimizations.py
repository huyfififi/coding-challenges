import collections
import itertools


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])

        board_char_to_count = collections.Counter(itertools.chain.from_iterable(board))
        word_char_to_count = collections.Counter(word)
        for ch in word_char_to_count:
            if board_char_to_count[ch] < word_char_to_count[ch]:
                return False

        if board_char_to_count[word[-1]] < board_char_to_count[word[0]]:
            word = "".join(reversed(word))

        def starts_from(
            row: int, col: int, word_idx: int, used: list[list[bool]]
        ) -> bool:
            if word_idx == len(word):
                return True

            if not (0 <= row < num_rows and 0 <= col < num_cols):
                return False
            if used[row][col]:
                return False
            if board[row][col] != word[word_idx]:
                return False

            result = False
            used[row][col] = True
            result |= starts_from(row + 1, col, word_idx + 1, used)
            result |= starts_from(row - 1, col, word_idx + 1, used)
            result |= starts_from(row, col + 1, word_idx + 1, used)
            result |= starts_from(row, col - 1, word_idx + 1, used)
            used[row][col] = False
            return result

        used = [[False] * num_cols for _ in range(num_rows)]
        for row in range(num_rows):
            for col in range(num_cols):
                if starts_from(row, col, 0, used):
                    return True

        return False
