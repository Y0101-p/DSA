from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def check(num,path):
            alist=dic[num]
            for i in alist:
                if i not in done_set:
                    if i in path:
                        return False
                    else:
                        path.append(i)
                        if not check(i,path):
                            return False
                        path.pop()
            done_set.add(num)
            return True
        dic={}
        for i in prerequisites:
            dic.setdefault(i[0],[]).append(i[1])
        done_set=set()
        for i in range(numCourses):
            if i not in dic:
                done_set.add(i)
        for i in dic:
            if not check(i,[i]):
                return False
        return True


if __name__=='__main__':
    soulution=Solution()
    res=soulution.canFinish(numCourses = 3, prerequisites = [[2,1],[1,0]])
    print(res)