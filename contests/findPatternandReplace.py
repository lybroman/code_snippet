class Solution(object):
	def findAndReplacePattern(self, words, pattern):
		def word_to_pattern(word):
			pattern_dict = {}
			idx = 1
			new_pattern = 0
			for ch in word:
				if ch in pattern_dict:
					new_pattern = new_pattern * 10 + pattern_dict[ch]
				else:
					new_pattern = new_pattern * 10 + idx
					pattern_dict[ch] = idx
					idx += 1

			return new_pattern

		pt =  word_to_pattern(pattern)

		ans = []
		for word in words:
			if word_to_pattern(word) == pt:
				ans.append(word)

		return ans




words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
print Solution().findAndReplacePattern(words, pattern)