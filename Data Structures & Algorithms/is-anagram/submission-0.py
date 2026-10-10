"""
Inputs: Two strings: s, t.

Output: Boolean value that returns true if the two strings are anagrams of each other, else returns False

Brute Force: You compare the two strings, character by character by making a list copy of one of them and comparing it to the other string. You loop through each element in the other string and use .remove() on thay element for the list copy. If the element being removed is not contained in the copied list, return false, else return true at the end of the loop. Space Complexity O(N), Time Complexity O(N^2)

Optimized Method: Create a dictionary that holds the counts of each unique character for one of the strings and then loop over the next string and subtract each count for each character seen in other string. If the character is not found or the count goes below 0, it is not an anagram. O(1), Time Complexity: O(N)

Arrays and Hashing problem (Frequency Mapping via Hash Table)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Anagrams have to be the same length
        if len(s) != len(t):
            return False

            
        counts = {}

        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        
        for ch in t:
            if ch not in counts or (counts[ch] - 1) < 0:
                return False
            counts[ch] -= 1
        
        return True
        