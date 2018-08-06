class Solution(object):
	def splitIntoFibonacci(self, S):
		ans = []

		max_split_digits = len(S) / 3

		def genetate_fb_seq(strs, ans):
			if not strs and len(ans) >= 3:
				return True
			elif not strs:
				return False

			for i in range(1, len(strs) + 1):
				if i > 1 and strs[0] == '0':
					return False
				elif int(strs[:i]) > 2**31 - 1:
					return False
				elif len(ans) < 2:
					ans.append(int(strs[:i]))
				elif ans[-1] + ans[-2] == int(strs[:i]):
					ans.append(int(strs[:i]))
				else:
					continue

				if genetate_fb_seq(strs[i:], ans):
					return True
				else:
					ans.pop(-1)

			return False

		for i in range(1, max_split_digits + 2):
			if i > 1 and S[0] == '0':
				continue
			ans.append(int(S[:i]))
			if genetate_fb_seq(S[i:], ans):
				return ans
			ans.pop(-1)

		return []


print Solution().splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511")