# 804. Unique Morse Code Words
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dicti = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        morse_words=[]
        for i in words:
            m_word=""
            for j in i:
                m_word+=dicti[j]
            morse_words.append(m_word)

        return len(list(set(morse_words)))


"""
Approach:
- I used a dictionary to map each letter to its Morse code.
- I then used a nested loop to iterate through the words and their corresponding Morse codes.
- For each word, I calculated the Morse code by concatenating the Morse codes of its letters.
- Finally, I returned the length of the set of Morse codes as the result.
"""
