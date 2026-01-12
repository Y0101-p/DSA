from typing import List
from collections import defaultdict
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def build_buckets(word):
            for i in range(8):
                bucket = f'{word[:i]}_{word[i+1:]}'
                buckets.setdefault(bucket, []).append(word)
        buckets = defaultdict(list)
        build_buckets(startGene)
        for word in bank:
            build_buckets(word)
        graph=defaultdict(list)
        for bucket in buckets:
            if len(buckets[bucket]) == 1:
                continue
            else:
                alist=buckets[bucket]
                for i in range(len(alist)):
                    for j in range(i+1, len(alist)):
                        graph.setdefault(alist[i], []).append(alist[j])
                        graph.setdefault(alist[j], []).append(alist[i])
        queue = deque([[startGene,0]])
        visited = set()
        while queue:
            pr,cnt = queue.popleft()
            for new_pr in graph[pr]:
                if new_pr == endGene:
                    return cnt+1
                if new_pr not in visited:
                    queue.append([new_pr,cnt+1])
            visited.add(pr)
        return -1