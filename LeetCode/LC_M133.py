from decorator import append


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node):
            new_node = Node(node.val)
            finished_set[node.val] = new_node
            for i in node.neighbors:
                if i.val not in finished_set:
                    new_node.neighbors.append(dfs(i))
                else:
                    new_node.neighbors.append(finished_set[i.val])

            return new_node


        finished_set = {}
        if node:
            return dfs(node)
        else:
            return None
"""邻接表
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def build_graph(node: Optional['Node']):
            if node.val in graph:
                return
            else:
                graph[node.val] = []
                for i in node.neighbors:
                    graph[node.val].append(i.val)
            for i in node.neighbors:
                build_graph(i)
                return

        graph={}
        build_graph(node)
        check_dic={}
        for i in graph:
            if i in check_dic:
                pr=check_dic[i]
            else:
                pr=Node(i)
                check_dic[i]=pr
            for j in graph[i]:
                if j in check_dic:
                    new_pr=check_dic[j]
                else:
                    new_pr=Node(j)
                pr.neighbors.append(new_pr)
                check_dic[j]=new_pr
        return check_dic[1]
"""

node=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node.neighbors=[node2,node4]
node2.neighbors=[node3,node]
node3.neighbors=[node4,node2]
node4.neighbors=[node3,node]
sol=Solution()
print(sol.cloneGraph(node))