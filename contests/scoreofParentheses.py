class Solution(object):
	def scoreOfParentheses(self, S):
		queue = []
		score = 0
		i = 0
		if len(S) == 2:
			return 1
		while i < len(S):
			if S[i] == '(':
				queue.append(S[i])
				i += 1
			else:
				j = i
				while j < len(S):
					if S[j] != ')':
						break
					queue.pop()
					j += 1

				score += 2 ** ((j - i - 1) + len(queue))
				i = j

		return score


print Solution().scoreOfParentheses('(()())')
print Solution().scoreOfParentheses('(()(()))')
print Solution().scoreOfParentheses('()')
print Solution().scoreOfParentheses('(())')
print Solution().scoreOfParentheses('((()))')
print Solution().scoreOfParentheses('((()(()))())')

