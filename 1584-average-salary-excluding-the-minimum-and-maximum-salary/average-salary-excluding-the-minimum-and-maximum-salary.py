class Solution:
    def average(self, salary: List[int]) -> float:
        mini=min(salary)
        maxi=max(salary)
        sum=0
        cnt=0
        for num in salary:
            if num!=mini and num!=maxi:
                sum+=num
                cnt+=1
        
           
        return sum/cnt