class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxi=0
        n=len(fruits)
        left,right=0,0
        my_dict={}
        while right<n:
            my_dict[fruits[right]]=my_dict.get(fruits[right],0)+1
            while len(my_dict)>2:
                my_dict[fruits[left]]-=1
                if my_dict[fruits[left]]==0:
                    del my_dict[fruits[left]]
                left+=1
            if len(my_dict)<=2:
                maxi=max(maxi,right-left+1)
            right+=1
        return maxi

        # max_len=0
        # n=len(fruits)
        # for i in range(n):
        #     mySet=set()
        #     for j in range(i,n):
        #         mySet.add(fruits[j])
        #         if len(mySet)>2:
        #             break
        #         max_len=max(max_len,j-i+1)
        # return max_len