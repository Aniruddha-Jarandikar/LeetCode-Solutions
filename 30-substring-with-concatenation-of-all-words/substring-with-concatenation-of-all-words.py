class Solution:
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = {}

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        total_words = len(words)
        total_len = word_len * total_words

        result = []

        # Try each possible starting offset
        for offset in range(word_len):

            left = offset
            right = offset
            current_count = {}
            words_used = 0

            while right + word_len <= len(s):

                word = s[right:right + word_len]
                right += word_len

                # Word is not present in words
                if word not in word_count:
                    current_count = {}
                    words_used = 0
                    left = right
                    continue

                current_count[word] = current_count.get(word, 0) + 1
                words_used += 1

                # Too many occurrences of this word
                while current_count[word] > word_count[word]:

                    left_word = s[left:left + word_len]
                    current_count[left_word] -= 1
                    left += word_len
                    words_used -= 1

                # All words are present
                if words_used == total_words:
                    result.append(left)

                    # Move window forward
                    left_word = s[left:left + word_len]
                    current_count[left_word] -= 1
                    left += word_len
                    words_used -= 1

        return result