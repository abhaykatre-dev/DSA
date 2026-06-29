class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        my_dict={
            "--X":-1,
            "X--":-1,
            "X++":1,
            "++X":1,
        }
        X=0
        for i in operations:
            if i in my_dict:
                X+=my_dict[i]
        return X