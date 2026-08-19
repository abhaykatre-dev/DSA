class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved={}
        for row,seat in reservedSeats:
            if row not in reserved:
                reserved[row]=set()
            reserved[row].add(seat)
        # empty row ke pass maximum 2 seats aa skti hai so hum total row me se vo row nikal de jo reserved hai to baki rows ke total grp nikal jayege
        ans=(n-len(reserved))*2
        for seats in reserved.values():
            left=True
            for seat in range(2,6):
                if seat in seats:
                    left=False
                    break
            middle=True
            for seat in range(4,8):
                if seat in seats:
                    middle=False
                    break
            right=True
            for seat in range(6,10):
                if seat in seats:
                    right=False
                    break
            if left and right :
                ans+=2
            elif middle or left or right:
                ans+=1
        return ans
            
