class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        num=[1,2,3,4,5,6,7,8,9]
        result=[]
        def func(index,total,subset):
            if len(subset)==k:
                if total==n:
                    result.append(subset.copy())
                return
            if len(subset)>k or total>n or index>=len(num):
                return 
            subset.append(num[index])
            func(index+1,total+num[index],subset)
            subset.pop()
            func(index+1,total,subset)
        func(0,0,[])
        return result
