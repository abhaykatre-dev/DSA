class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def func(index,subset):
            if index>=len(nums):
                result.append(subset.copy())
                return
                
            subset.append(nums[index])
            func(index+1,subset)

            subset.pop()
            func(index+1,subset)
        
        func(0,[])
        return result
            
        # n=len(nums)
        # total_subset=1<<n  #2^n
        # result=[]
        # for num in range(total_subset):
        #     temp=[]
        #     for i in range(n):
        #         if num&(1<<i)!=0:
        #             temp.append(nums[i])
               
        #     result.append(temp)
        # return result   #TC=O(n*2^n) and SC = O(n*2^n)