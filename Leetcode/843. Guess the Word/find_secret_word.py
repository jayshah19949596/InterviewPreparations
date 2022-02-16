# From Leetcode Python android app

# https://leetcode.com/problems/guess-the-word/
# This problem is an interactive problem new to the LeetCode platform.
# We are given a word list of unique words, each word is 6 letters
# long, and one word in this list is chosen as secret.
# You may call master.guess(word) to guess a word.
# The guessed word should have type string and must
# be from the original list with 6 lowercase letters.
# This function returns an integer type, representing the number
# of exact matches (value and position) of your guess
# to the secret word.  Also, if your guess is not
# in the given wordlist, it will return -1 instead.
# For each test case, you have 10 guesses to guess the word.
# At the end of any number of calls, if you have made 10
# or less calls to master.guess and at least one of these
# guesses was the secret, you pass the testcase.
# Besides the example test case below, there will be 5 additional
# test cases, each with 100 words in the word list.
# The letters of each word in those testcases were
# chosen independently at random from 'a' to 'z',
# such that every word in the given word lists is unique.

# Repeatedly choose a word to guess and eliminate all words
# that do not have the same number of matches as the
# chosen word. Words are chosen so they have maximum overlap
# (same chars in same positions) with other words.
# This reduces candidate list more than choosing a random
# word which may not overlap with any other words and so
# does not allow any other words to be eliminated.
# Time - O(n)
# Space - O(n)

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

from collections import defaultdict
class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """

        def pair_matches(a, b):  # count the number of matching characters
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        def most_overlap_word():
            counts = [defaultdict(int) for _ in range(6)]  # counts[i] maps chars to count of words with char at index i

            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][c] += 1  # all words with same chars in same positions

            return max(candidates, key=lambda x: sum(counts[i][c] for i, c in enumerate(x)))

        candidates = wordlist[:]  # all remaining candidates, initially all words

        while candidates:
            guessed_word = most_overlap_word()  # guess the word that overlaps with most others
            matches = master.guess(guessed_word)
            if matches == 6:
                return
            candidates = [word for word in candidates if pair_matches(guessed_word, word) == matches] # filter words with same matches

