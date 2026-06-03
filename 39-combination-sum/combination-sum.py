class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def func(index,total,subset):
            if total==target:
                result.append(subset.copy())
                return
            if total>target or index>=len(candidates):
                return

            subset.append(candidates[index])
            func(index,total+candidates[index],subset)
            subset.pop()

            func(index+1,total,subset)
        func(0,0,[])
        return result