class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new_arr=sorted(arr)
        my_dict={}
        cnt=1
        for num in new_arr:
            if num not in my_dict:
                my_dict[num]=cnt
                cnt+=1
            
        ans=[]
        for num in arr:
            ans.append(my_dict[num])
        return ans