class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1=list(map(int,version1.split('.')))
        list2=list(map(int,version2.split('.')))
        pr=0
        lenth1=len(list1)
        lenth2=len(list2)
        while pr<max(lenth1,lenth2):
            if pr<min(lenth1,lenth2):
                a=list1[pr]
                b=list2[pr]
            elif lenth1>lenth2:
                a=list1[pr]
                b=0
            elif lenth1<lenth2:
                a=0
                b=list2[pr]
            if a<b:
                return -1
            elif a>b:
                return 1
            pr +=1
        return 0
