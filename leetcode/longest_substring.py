# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
# https://www.geeksforgeeks.org/window-sliding-technique/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:     
        startCurrentSubstringIndex = 0 # starting index for moving substring window
        longestSubstring = 0 # counts max size of window, which function will return
        hash = {}
        
        for currentIndex in range(0, len(s)): # iterate through each element in array

            if s[currentIndex] in hash: # if char is in the hash map already,
                indexLastOccurrence = hash[s[currentIndex]] # get last occurence
                startCurrentSubstringIndex = max(indexLastOccurrence + 1, startCurrentSubstringIndex) # move pointer 
            
            currentSubStringLength = (currentIndex - startCurrentSubstringIndex) + 1
            longestSubstring = max(longestSubstring, currentSubStringLength) # increment counter if higher
            
            hash[s[currentIndex]] = currentIndex # replace the value in the hash map with the index

        return longestSubstring
            

        