class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for i in range(1,numRows+1):
            tempVal=[]
            x=1
            for j in range(1,i+1):
                tempVal.append(x)
                x=int(x*(i-j)/j)
            result.append(tempVal)
        return result