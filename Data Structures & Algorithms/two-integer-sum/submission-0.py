"""
Inputs: nums (array of integers), target (integer)

Outputs: Indices (i, j) of the integers that sum up to target in increasing order

Brute Force: There will be one loop iterating through all the integers in nums (tracked by i), and there will another nested loop within that (tracked by j, starting at the position i + 1), and the nested loop will check the sum of the integers at the i and every j index within the loop until the sum is found. 
Space Complexity: O(1), Time Complexity: O(N^2)

Optimal Solution: I will keep a dictionary. I will iterate through nums and find the difference between the target value and the current integer and check if that difference is in my dictionary already. If it is, I have my two indices, and if it isn't, I will add that integer paired with its index to the dictionary.
Space Complexity: O(N), Time Complexity: O(N)

This is an array and hashing problem (Mapping via hash table)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen:
                return [seen[diff], i]
            
            seen[n] = i
