class Solution {
  // Define a method to remove duplicate elements from an array in-place
  removeDuplicates(nums) {
      // Convert the array to a Set to automatically remove duplicates
      const set = new Set(nums);
      
      // Clear the original array
      nums.length = 0;
      
      // Spread the unique elements from the Set into the original array
      nums.push(...set);
      
      // Sort the array (optional, depends on whether you want the result to be sorted)
      nums.sort((a, b) => a - b);
      
      // Return the length of the modified array (number of unique elements)
      return nums.length;
  }
}

// Example usage:
const solution = new Solution();
const inputArray = [1, 2, 3, 2, 4, 5, 6, 5, 7];
const resultLength = solution.removeDuplicates(inputArray);

console.log(inputArray); // Modified array with unique elements
console.log(resultLength); // Number of unique elements in the array
