class Solution:
    def fullJustify(self, words, maxWidth):
        """
        Given a list of words and a maximum width maxWidth, format the text 
        such that each line has exactly maxWidth characters and is 
        fully (left and right) justified. Words should be packed in a greedy approach.
        """
        justified_text = []  # Resultant list that will contain the fully justified text
        current_index, total_words = 0, len(words)  # Initialize current index and get the total number of words
      
        # Iterate over words to construct each line
        while current_index < total_words:
            line_words = []  # Words to be included in the current line
            count = len(words[current_index])  # Character count in the current line, starting with the first word
            line_words.append(words[current_index])  # Add first word to the line
            current_index += 1  # Move to the next word
          
            # Try to fit as many words as possible into the current line
            while current_index < total_words and count + 1 + len(words[current_index]) <= maxWidth:
                count += 1 + len(words[current_index])  # Update count including spaces between words
                line_words.append(words[current_index])  # Add next word to the line
                current_index += 1  # Move to the next word
          
            # Check if it's the last line or contains only one word
            if current_index == total_words or len(line_words) == 1:
                # Left-justify the line
                line_left_justified = ' '.join(line_words)
                # Calculate the remaining spaces on the right
                spaces_on_right = ' ' * (maxWidth - len(line_left_justified))
                # Add the left-justified and right-padded line to result
                justified_text.append(line_left_justified + spaces_on_right)
                continue
          
            # Not the last line or a single word, fully justify the line
            total_spaces = maxWidth - (count - len(line_words) + 1)  # Calculate total spaces to fill
            space_width, extra_spaces = divmod(total_spaces, len(line_words) - 1)  # Evenly distribute spaces
          
            constructed_line = []
            # Distribute space_width (+1 for extra_spaces) among words
            for index, word in enumerate(line_words[:-1]):
                constructed_line.append(word)
                # Append the appropriate number of spaces after the current word
                constructed_line.append(' ' * (space_width + (1 if index < extra_spaces else 0)))
              
            constructed_line.append(line_words[-1])  # Append the last word without extra spaces
            justified_text.append(''.join(constructed_line))  # Add the fully justified line to result
          
        return justified_text  # Return the justified text as a list of lines