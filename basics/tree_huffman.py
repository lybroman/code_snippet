# Huffman Tree
from heapq import heapify, heappush, heappop
from itertools import count


def huffman(seq, frq):
	num = count()
	trees = zip(frq, num, seq)
	heapify(trees)
	while len(trees) > 1:
		fa, _, a = heappop(trees)
		fb, _, b = heappop(trees)
		n = next(num)
		heappush(trees, (fa + fb, n, [a, b]))

	return trees[0][-1]


frq = [4, 5, 6, 9, 11, 12, 15, 16, 20]
seq = 'abcdefghi'

huffman_tree = huffman(seq, frq)


def codecs(tree, prefix=''):
	if len(tree) == 1:
		yield tree, prefix
		return

	for subtree, bit in zip(tree, '01'):
		for code, prefix in codecs(subtree, prefix + bit):
			yield code, prefix


for code, prefix in codecs(huffman_tree, "b"):
	print code, ':', prefix
