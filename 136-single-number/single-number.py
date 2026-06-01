class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #O(N+N/2+1)=O(N) , SC=O(N)
        # my_dict={}
        # for num in nums:
        #     my_dict[num]=my_dict.get(num,0)+1
        # for key in my_dict:
        #     if my_dict[key]==1:
        #         return key

        #SC=O(1)
        result=0
        for num in nums:
            result^=num
        return result
