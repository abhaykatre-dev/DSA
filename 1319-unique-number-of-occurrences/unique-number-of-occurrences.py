class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_set=set()
        for num in set(arr):
            count=arr.count(num)
            if count in my_set:
                return False
            my_set.add(count)
        return True