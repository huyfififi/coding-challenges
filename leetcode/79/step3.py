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

        if word_char_to_count[word[-1]] < word_char_to_count[word[0]]:
            word = word[::-1]

        def traverse(row: int, col: int, word_idx: int, used: list[list[int]]) -> bool:
            if word_idx == len(word):
                return True

            if not (0 <= row < num_rows and 0 <= col < num_cols):
                return False
            if used[row][col]:
                return False
            if board[row][col] != word[word_idx]:
                return False

            found = False
            used[row][col] = True
            found |= traverse(row + 1, col, word_idx + 1, used)
            found |= traverse(row - 1, col, word_idx + 1, used)
            found |= traverse(row, col + 1, word_idx + 1, used)
            found |= traverse(row, col - 1, word_idx + 1, used)
            used[row][col] = False
            return found

        used = [[False] * num_cols for _ in range(num_rows)]
        for row in range(num_rows):
            for col in range(num_cols):
                if traverse(row, col, 0, used):
                    return True

        return False
