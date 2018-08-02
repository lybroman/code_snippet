class Solution(object):
	def backspaceCompare(self, S, T):
		i = len(S) - 1
		j = len(T) - 1

		si_r_count = 0
		sj_r_count = 0
		while i >= 0 and j >= 0:
			while i >= 0 and (S[i] == '#' or si_r_count > 0):
				si_r_count += 1 if S[i] == '#' else -1
				i -= 1

			while j >= 0 and (T[j] == '#' or sj_r_count > 0):
				sj_r_count += 1 if T[j] == '#' else -1
				j -= 1

			print i, j, S[i], T[j]

			if i < 0 and j < 0:
				return True
			elif i >= 0 and j >= 0 and S[i] == T[j]:
				i -= 1
				j -= 1
				continue
			else:
				return False

		print i, j

		while i >= 0 and (S[i] == '#' or si_r_count > 0):
			si_r_count += 1 if S[i] == '#' else -1
			i -= 1

		while j >= 0 and (T[j] == '#' or sj_r_count > 0):
			sj_r_count += 1 if T[j] == '#' else -1
			j -= 1

		if i >= 0 or j >= 0:
			return False

		return True


S = "bbbextm"
T = "bbb#extm"

print Solution().backspaceCompare(S, T)
