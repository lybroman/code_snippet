import heapq
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]


def generate_skyline(buildings):
	events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
	res, hp = [[0, 0]], [(0, float("inf"))]
	for x, negH, R in events:
		while x >= hp[0][1]:
			heapq.heappop(hp)
		if negH:
			heapq.heappush(hp, (negH, R))
		if res[-1][1] + hp[0][0]:
			# list += extend the list
			res += [x, -hp[0][0]],
	return res[1:]


print generate_skyline(buildings)


hp = [3, 1, 2, 0, 8, 9]
heapq.heapify(hp)
print hp

# private method
heapq._heapify_max(hp)
print hp



