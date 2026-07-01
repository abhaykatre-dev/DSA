class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        curr = head

        while curr:
            if curr.val in nums and (curr.next is None or curr.next.val not in nums):
                ans += 1
            curr = curr.next

        return ans