from typing import List
from collections import deque

class SolutionBfs:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = {i:0 for i in range(numCourses)}
        graph = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            in_degree[prerequisite[0]] += 1
        result = []
        que=deque()
        for i in in_degree:
            if in_degree[i] == 0:
                que.append(i)
        while que:
            node = que.popleft()
            result.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    que.append(neighbor)
        if len(result) != numCourses:
            return []
        return result

class SolutionDfs:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node):
            if hax[node]==2:
                return True
            if hax[node]==1:
                return False
            hax[node] = 1
            if not graph[node]:
                hax[node] = 2
                stack.append(node)
                return True
            for i in graph[node]:
                if not dfs(i):
                    return False
            hax[node] = 2
            stack.append(node)
            return True


        graph = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
        hax=[0]*numCourses
        stack=[]
        for i in range(numCourses):
            if not dfs(i):
                return []
        return stack[::-1]