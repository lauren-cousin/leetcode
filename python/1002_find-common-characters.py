# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
#
# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
#
# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
#
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
#
# Difficulty: Easy
# Tags: Array, Hash Table, String
# Time Complexity: O(N * M * L) – because the function iterates over each unique character in the first word (O(M)) and counts its occurrences in every word (O(N * L)).
# Space Complexity: O(M * N) – because the function uses space to store the unique characters from the first word (O(M)) and the result list that could grow up to O(M * N) in size.

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 0:
            # If the input list is empty, return an empty list.
            return []
        if len(words) == 1:
            # If there's only one word, return each character as a separate element in the list, including duplicates.
            return list(words[0])
        chars_in_all_strings = []
        first_word = set(words[0])  # check each unique character in first word
        for letter in first_word:
            frequency = min(
                [word.count(letter) for word in words])  # calc minimum freq of that char across all words in list
            chars_in_all_strings += [letter] * frequency  # char added as many times as it appears in every list
        return chars_in_all_strings


