"""
Input: array of integers. Question does not specify whether integers are ordered, so I will assume they are unordered/random.

Output: Bool value expressing true if there is a duplicate integer in the set and false if there isn't

Brute Force: You can use one loop to loop i over the indices of nums and use another nested loop to loop j over the indices of i + 1, so you start from the next position each time and compare the number at index j to the rest of the numbers in the nested loop. Space Complexity: O(1), Time Complexity: O(N^2)

Optimized Method: Loop through nums and store each element in a set and check if an element is already in a set. If it is, that means there is a duplicate in nums, and if there isn't then I return false. Space Complexity: O(N), Time Complexity: O(N)

Even though the space complexity is better for Brute Force, when it comes to a tradeoff, we should prioritize runtime over space used.

Arrays and Hashing problem (Uniqueness Tracking via Hash Table).
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for n in nums:
            if n not in seen:
                seen.add(n)

            else:
                return True
        
        return False
        