class Solution(object):
	def shiftingLetters(self, S, shifts):
		ss= list(S)
		for ii, shift in enumerate(shifts):
			for i in xrange(ii + 1):
				v = (ord(ss[i]) - ord('a') + shift) % 26
				ss[i] = chr(ord('a') + v)

		return ''.join(ss)

	def shiftingLetters1(self, S, shifts):
		if not shifts: return S
		all_shifts = [shifts[-1]]
		for i in xrange(len(shifts) - 2, -1, -1):
			all_shifts.append(all_shifts[-1] + shifts[i])

		all_shifts.reverse()

		ss = list(S)
		for ii, shift in enumerate(all_shifts):
			v = (ord(ss[ii]) - ord('a') + shift) % 26
			ss[ii] = chr(ord('a') + v)

		return ''.join(ss)

print Solution().shiftingLetters1('abc', [3,5,9])



