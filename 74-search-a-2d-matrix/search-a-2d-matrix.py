class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for list in matrix:
            if target<=list[-1]:
                l,r=0,len(list)-1
                while l<=r:
                    mid=(l+r)//2
                    if list[mid]==target:
                        return True
                    elif target<list[mid]:
                        r=mid-1
                    else:
                        l=mid+1
                return False
        return False