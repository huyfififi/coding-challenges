class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # `|` の挿入により、全ての回文の長さが奇数になり、統一的に扱える
        # |a|b|a| -> b が中心
        # |a|b|b|a| -> | が中心
        s_with_separators: list[str] = ["|"]
        for c in s:
            s_with_separators.append(c)
            s_with_separators.append("|")
        transformed = "".join(s_with_separators)

        # palindrome_radii[i] -> i を中心とした最長の回文の半径
        # TIL radii is the plural form of radius
        palindrome_radii = [0] * len(transformed)

        center = 0
        radius = 0

        while center < len(transformed):  # 各中心を順に見ていく
            while (  # 左右が範囲内にある かつ 左端と右端の文字が一致する 間 半径を広げる
                center - (radius + 1) >= 0
                and center + (radius + 1) < len(transformed)
                and transformed[center - (radius + 1)]
                == transformed[center + (radius + 1)]
            ):
                radius += 1

            palindrome_radii[center] = radius

            old_center = center
            old_radius = radius

            # center を中心とした最大半径はわかっているので、今度はその結果を利用しながら
            # center + 1 以降をチェックしていく
            center += 1
            radius = 0

            while center <= old_center + old_radius:
                mirrored_center = old_center - (center - old_center)
                # center から old_center を中心とする回文の右端までの距離
                # i.e., mirrored_center から old_center を中心とする回文の左端までの距離
                max_mirrored_radius = old_center + old_radius - center

                # center を右に動かしていく過程で、
                # palindrome_radii[mirrored_center] は 既知

                # mirrored_center を中心とする回文が完全に
                # old_centerを中心とする最大長の回文に収まっている時
                # (max_mirrored_radius = mirrored_center から old_centerを中心とする最長回文の左端までの距離)
                if palindrome_radii[mirrored_center] < max_mirrored_radius:
                    # 左右対称なので
                    palindrome_radii[center] = palindrome_radii[mirrored_center]
                    center += 1
                # mirrored_center を中心とする回文が
                # old_center を中心とする最大長の回文に収まっていない時
                elif palindrome_radii[mirrored_center] > max_mirrored_radius:
                    # 左右対称なので、mirrored_center から 大きな回文の左端を半径とした回文が
                    # center を中心にしても現れる
                    palindrome_radii[center] = max_mirrored_radius
                    center += 1
                else:
                    # palindrome_radii[mirrored_center] == max_mirrored_radius
                    # i.e., center を中心とする回文の右端が、既知の大きな回文の右端と一致
                    radius = max_mirrored_radius
                    break

        # 各中心の回文半径の中で最大のものを探す
        max_center = 0
        max_radius = 0
        for center, radius in enumerate(palindrome_radii):
            if radius > max_radius:
                max_center = center
                max_radius = radius

        start = (max_center - max_radius) // 2
        end = start + max_radius
        return s[start:end]
