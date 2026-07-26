class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # nums.sort()
        # return max(
        #     nums[-1] * nums[-2] * nums[-3],  # three largest
        #     nums[0] * nums[1] * nums[-1]     # two smallest + largest
        # )

        largest = second = third = float('-inf')
        smallest = second_smallest = float('inf')

        for num in nums:
            if num>largest:
                third=second
                second=largest
                largest=num
            elif num>second:
                third=second
                second=num
            elif num>third:
                third=num
            if num<smallest:
                second_smallest=smallest
                smallest=num
            elif num<second_smallest:
                second_smallest=num
        return max(largest*second*third,smallest*second_smallest*largest)