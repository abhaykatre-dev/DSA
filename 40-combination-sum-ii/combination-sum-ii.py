class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def backTrack(index,total,subset):
            if total==0:
                result.append(subset.copy())
                return
            if total<0 or index>len(candidates):
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i-1]==candidates[i]:
                    continue
                subset.append(candidates[i])
                backTrack(i+1,total-candidates[i],subset)
                subset.pop()
        backTrack(0,target,[])
        return result
    # bruteforce 
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     candidates.sort()
    #     result=set()
    #     self.func(candidates,target,result,0,0,[])
    #     return [list(x) for x in result]
    
    # def func(self,nums,target,result,index,total,subset):
    #     if total==target:
    #         result.add(tuple(subset))
    #         return
    #     if total>target or index>=len(nums):
    #         return
    #     subset.append(nums[index])
    #     self.func(nums,target,result,index+1,total+nums[index],subset)
    #     subset.pop()
    #     self.func(nums,target,result,index+1,total,subset)
        