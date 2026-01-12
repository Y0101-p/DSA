from typing import List
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(path,nums,haxdic,i,k):
            if i==len(nums):
                if path==[]:
                    return
                ans[0] +=1
                return
            if haxdic.setdefault(nums[i]-k,0)==0 and haxdic.setdefault(nums[i]+k,0)==0:
                haxdic.setdefault(nums[i],0)
                haxdic[nums[i]] +=1
                path.append(nums[i])
                dfs(path,nums,haxdic,i+1,k)
                path.pop()
                haxdic[nums[i]] -=1
            dfs(path,nums,haxdic,i+1,k)
            return
        ans=[0]
        haxdic={}
        dfs([],nums,haxdic,0,k)
        return ans[0]


if __name__ == '__main__':
    solution = Solution()
    res = solution.beautifulSubsets(nums = [2,4,6], k = 2)
    print(res)