from bisect import bisect_right
from collections import Counter, defaultdict, deque
import collections
import heapq
import math
import sys
import re
from typing import List


from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        N = len(isConnected)
        used = [False] * N
        provences = 0

        def traverse(start):
            q = deque()
            q.append(start)

            while q:
                current = q.popleft()
                for connected_city in range(N):
                    if isConnected[current][connected_city] and not used[connected_city]:
                        q.append(connected_city)
                        used[connected_city] = True

        for city in range(N):
            if not used[city]:
                used[city] = True
                provences += 1
                traverse(city)
        return provences
            
                        
sol = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
sol.findCircleNum(isConnected)
