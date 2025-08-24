# 733. Flood Fill
# Link: https://leetcode.com/problems/flood-fill/
# Difficulty: Easy
# Tags: Array, BFS, DFS, Matrix

from typing import List
from queue import Queue

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = Queue()
        q.put((sr, sc))
        original = image[sr][sc]

        while not q.empty():
            i, j = q.get()
            image[i][j] = color
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(image) and 0 <= nj < len(image[0]) and image[ni][nj] == original:
                    q.put((ni, nj))

        return image
