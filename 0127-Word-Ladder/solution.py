class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if endWord not in wordList:
            return 0

        word_set = set(wordList)
        queue = deque([(beginWord, 1)])

        while queue:
            curr_word, step = queue.popleft()

            for i in range(len(curr_word)):
                for letter in string.ascii_lowercase:
                    temp_word = curr_word[:i] + letter + curr_word[i + 1:]

                    if temp_word == endWord:
                        return step + 1

                    if temp_word in word_set:
                        word_set.remove(temp_word)
                        queue.append((temp_word, step + 1))

        return 0


