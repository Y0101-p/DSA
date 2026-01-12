from collections import defaultdict
import heapq
import itertools

class Graph:
    def __init__(self):
        self.check_dict = None
        self.graph=defaultdict(dict)

    def add_edge(self,u,v,w):
        self.graph[u][v]=w
        self.graph[v][u]=w

    def dijkstra(self,start,end):
        heap=[]
        cnt=itertools.count()
        heapq.heappush(heap,(0,next(cnt),[start]))
        path_dic={start:0}
        finished=set()
        while heap:
            distance,count,path=heapq.heappop(heap)
            u=path[-1]
            if u in finished:
                continue
            if u==end:
                break
            finished.add(u)
            for v,w in self.graph[u].items():
                if v in finished:
                    continue
                if v in path_dic:
                    new_distance=distance+w
                    if new_distance < path_dic[v]:
                        path_dic[v]=new_distance
                        heapq.heappush(heap,(new_distance,next(cnt),path+[v]))
                else:
                    path_dic[v]=distance+w
                    heapq.heappush(heap,(distance+w,next(cnt),path+[v]))
        res=''
        for i in range(len(path)-1):
            res+=path[i]+f'->({self.graph[path[i]][path[i+1]]})->'
        res+=path[-1]
        return res
    def floyd_warshall(self):
        cnt=itertools.count()
        check_dict={}
        for pr in self.graph:
            check_dict[pr]=next(cnt)
            check_dict[check_dict[pr]]=pr
        self.check_dict=check_dict
        n=len(check_dict)//2
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        next_node=[[-1]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    dist[i][j] = 0
                    next_node[i][j] = j
                elif check_dict[j] in self.graph[check_dict[i]]:
                    dist[i][j] = self.graph[check_dict[i]][check_dict[j]]
                    next_node[i][j] = j

            # Floyd-Warshall算法核心
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]

        return dist, next_node

    def construct_shortest_path(self, start, end, next_node):
        start,end=self.check_dict[start],self.check_dict[end]
        if next_node[start][end] == -1:
            return []

        path = [self.check_dict[start]]
        current = start

        while current != end:
            current = next_node[current][end]
            path.append(self.check_dict[current])

        res=''
        for i in range(len(path)-1):

            res += path[i] + f'->({self.graph[path[i]][path[i + 1]]})->'
        res += path[-1]
        return res


if __name__=='__main__':
    graph=Graph()
    p=int(input())
    name=[]
    for i in range(p):
        name.append(input())
    q=int(input())
    for i in range(q):
        u,v,w=input().split()
        graph.add_edge(u,v,int(w))
    r=int(input())
    dist,next_node=graph.floyd_warshall()
    for i in range(r):
        start,end=input().split()
        print(graph.construct_shortest_path(start,end,next_node))