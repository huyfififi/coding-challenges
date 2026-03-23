import collections
import itertools


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])

        board_char_to_count = collections.Counter(itertools.chain.from_iterable(board))
        word_char_to_count = collections.Counter(word)
        for ch in word_char_to_count:
            if word_char_to_count[ch] > board_char_to_count[ch]:
                return False

        if board_char_to_count[word[-1]] < board_char_to_count[word[0]]:
            word = word[::-1]

        def traverse(row: int, col: int, char_idx: int, used: list[list[bool]]) -> bool:
            if char_idx == len(word):
                return True

            if not (0 <= row < num_rows and 0 <= col < num_cols):
                return False
            if used[row][col]:
                return False
            if board[row][col] != word[char_idx]:
                return False

            used[row][col] = True
            if (
                traverse(row + 1, col, char_idx + 1, used)
                or traverse(row - 1, col, char_idx + 1, used)
                or traverse(row, col + 1, char_idx + 1, used)
                or traverse(row, col - 1, char_idx + 1, used)
            ):
                used[row][col] = False
                return True

            used[row][col] = False
            return False

        used = [[False] * num_cols for _ in range(num_rows)]
        for row in range(num_rows):
            for col in range(num_cols):
                if traverse(row, col, 0, used):
                    return True

        return False
