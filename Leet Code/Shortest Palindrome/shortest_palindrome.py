class Solution:
    def shortestPalindrome(self, s: str) -> str:
        base = 131  # Base for polynomial rolling hash.
        mod = 10**9 + 7  # Modulus for hash to avoid overflow.
        n = len(s)  # Length of the input string.
        prefix_hash = 0  # Hash value of the prefix.
        suffix_hash = 0  # Hash value of the suffix.
        multiplicator = 1  # Multiplicator value used for hash computation.
        longest_palindrome_idx = 0  # End index of the longest palindromic prefix.

        # Compute rolling hash from both ends.
        for i, ch in enumerate(s):
            # Update the prefix hash by appending character.
            prefix_hash = (prefix_hash * base + (ord(ch) - ord('a') + 1)) % mod

            # Update the suffix hash by adding character (considered at the beginning).
            suffix_hash = (suffix_hash + (ord(ch) - ord('a') + 1) * multiplicator) % mod

            # Update the multiplicator for the next character.
            multiplicator = (multiplicator * base) % mod
          
            # If the prefix and suffix hashes match, update the longest prefix palindrome index.
            if prefix_hash == suffix_hash:
                longest_palindrome_idx = i + 1

        # If the entire string is a palindrome, return it.
        if longest_palindrome_idx == n:
            return s

        # Otherwise, append the reverse of the remaining suffix to the front to make the shortest palindrome.
        return s[longest_palindrome_idx:][::-1] + s