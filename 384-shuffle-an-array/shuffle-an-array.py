import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original=nums[:]
        self.nums=nums

    def reset(self) -> List[int]:
        self.nums=self.original
        return self.nums

    def shuffle(self) -> List[int]:
        n=len(self.nums)
        arr=self.nums[:]
        for i in range(n):
            j=random.randint(i,n-1)
            arr[i],arr[j]=arr[j],arr[i]
        self.nums=arr
        return self.nums
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()