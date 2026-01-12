from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            if len(stack)==0:
                stack.append((temperatures[i],i))
            else:
                while temperatures[i]>stack[-1][0]:
                    res[stack[-1][1]]=i-stack[-1][1]
                    stack.pop()
                    if len(stack)==0:
                        break
                stack.append((temperatures[i],i))
        return res
                    



if __name__ == '__main__':
    solution = Solution()
    mat = [73,74,75,71,69,72,76,73]
    res = solution.dailyTemperatures( mat)
    print(res)