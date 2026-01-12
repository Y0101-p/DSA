from typing import List
import statistics
import math
class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:

        def judge(left, right):
            if left == right:
                return 0
            else:
                if judge_list[right]>left:
                    return -1
                cache=cnt_list[left:right+1]
                mid=statistics.median(cache)
                cnt1=0
                cnt2=0
                if len(cache)%2==0:
                    mid1=math.ceil(mid)
                    mid2=math.floor(mid)
                    for i in cache:
                        cnt1+=abs(i-mid1)
                        cnt2+=abs(i-mid2)
                    return min(cnt1,cnt2)
                else:
                    for i in cache:
                        cnt1+=abs(i-mid)
                    return cnt1

        mod_list = []
        cnt_list = []
        for num in nums:
            mod_list.append(num%k)
            cnt_list.append(num//k)
        judge_list=[0]
        for i in range(1,len(mod_list)):
            if mod_list[i]==mod_list[judge_list[-1]]:
                judge_list.append(judge_list[-1])
            else:
                judge_list.append(i)
        res=[]
        for left, right in queries:
            res.append(judge(left, right))
        return res