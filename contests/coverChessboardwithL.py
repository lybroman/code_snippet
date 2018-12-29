import pprint
tag = 0
k = 2
chessboard = [[-1] * 2 ** k for _ in range(2 ** k)]


def cover(i, j, p, q, s):
	if s == 1:
		return
	s = s / 2

	global tag
	tag += 1
	t = tag

	# top right
	if p < i + s and q < j + s:
		cover(i, j, p, q, s)
	else:
		chessboard[i + s - 1][j + s - 1] = t
		cover(i, i + s - 1, p, j + s - 1, s)

	# top left
	if p < i + s and q >= j + s:
		cover(i, j + s, p, q, s)
	else:
		chessboard[i + s - 1][j + s] = t
		cover(i, j + s, i + s - 1, j + s, s)

	# bottom left
	if p >= i + s and q < j + s:
		cover(i + s, j, p, q, s)
	else:
		chessboard[i + s][j + s - 1] = t
		cover(i + s, j, i + s, j + s - 1, s)

	# bottom right
	if p >= i + s and q >= j + s:
		cover(i + s, j + s, p, q, s)
	else:
		chessboard[i + s][j + s] = t
		cover(i + s, j + s, i + s, j + s, s)


cover(0, 0, 0, 0, 4)

pprint.pprint(chessboard)