class Solution:
    # Define a method to remove duplicate elements from a list in-place
    def removeDuplicates(self, nums: list[int]) -> int:
        # Convert the list to a set to automatically remove duplicates
        list_set = set(nums)
        
        # Clear the original list
        nums.clear()
        
        # Extend the list with the unique elements from the set
        nums.extend(list_set)
        
        # Sort the list (optional, depends on whether you want the result to be sorted)
        nums.sort()
        
        # Return the length of the modified list (number of unique elements)
        return len(nums)
