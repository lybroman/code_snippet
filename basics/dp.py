# longest increasing sub-sequence
seq = [1, 0, 2, 4, 3, 7, 9, 8, 11]

# O(n^2)
def lis(seq):
	L = [1] * len(seq)
	for  cur in xrange(len(seq)):
		for prev in xrange(cur):
			if seq[prev] < seq[cur]:
				L[cur] = max(L[cur], L[prev] + 1)
	return L[-1]


print lis(seq)


# O(nlogn)
import bisect


def lis_1(seq):
	L = []
	for val in seq:
		idx = bisect.bisect(L, val)
		if idx >= len(L):
			L.append(val)
		else:
			L[idx] = val

	return len(L)

print lis_1(seq)






