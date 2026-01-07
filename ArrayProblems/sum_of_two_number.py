class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        # Iterate over the array
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If found, return the indices of the complement and the current number
                return [num_to_index[complement], i]

            # Store the current number and its index in the dictionary
            num_to_index[num] = i

        # If no solution is found (though the problem states there will always be one)
        return []
