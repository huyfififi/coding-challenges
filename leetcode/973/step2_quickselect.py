import random


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance_and_points: list[tuple[int, list[int]]] = []
        for x, y in points:
            distance_and_points.append((pow(x, 2) + pow(y, 2), [x, y]))

        def move_k_closest_points_to_left(left: int, right: int) -> None:
            if left == right:
                return

            pivot_index = random.randint(left, right)
            pivot_value = distance_and_points[pivot_index][0]
            distance_and_points[pivot_index], distance_and_points[right] = (
                distance_and_points[right],
                distance_and_points[pivot_index],
            )
            store_index = left
            for i in range(left, right):
                distance = distance_and_points[i][0]
                if distance < pivot_value:
                    distance_and_points[i], distance_and_points[store_index] = (
                        distance_and_points[store_index],
                        distance_and_points[i],
                    )
                    store_index += 1
            distance_and_points[store_index], distance_and_points[right] = (
                distance_and_points[right],
                distance_and_points[store_index],
            )

            if store_index == k - 1:
                return
            elif store_index < k - 1:
                move_k_closest_points_to_left(store_index + 1, right)
            else:
                move_k_closest_points_to_left(left, store_index - 1)

        move_k_closest_points_to_left(0, len(distance_and_points) - 1)
        return [point for _, point in distance_and_points[:k]]
