class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ch_map={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        result=[]
        def func(index,subset):
            if index==len(digits):
                result.append("".join(subset))
                return
            for ch in ch_map[digits[index]]:
                subset.append(ch)
                func(index+1,subset)
                subset.pop()
        func(0,[])
        return result