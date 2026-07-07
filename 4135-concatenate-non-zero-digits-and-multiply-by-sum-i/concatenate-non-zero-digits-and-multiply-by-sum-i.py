class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digit_sum=0
        digits=[]
        while n>0:
            LD=n%10
            if LD!=0:
                digits.append(str(LD))
                digit_sum+=LD
            n=n//10
        num=int("".join(digits[::-1])) if digits else 0
        return num*digit_sum 
