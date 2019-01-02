nums = [1, 2, 5, 3, 4, 6, 8, 9, 7, 0]


def insert_sort(target):
	target = target[:]
	for i in xrange(1, len(target)):
		j = i - 1
		key = target[i]
		while j >= 0 and key < target[j]:
			target[j + 1] = target[j]
			target[j] = key
			j -= 1
	return target


def shell_sort(target):
	target = target[:]
	step = 2
	group = len(target) / step

	while group:
		for i in xrange(group):
			j = i + group
			while j < len(target):
				k = j - group
				key = target[j]
				while k >= 0 and target[k] > key:
					target[k + group] = target[k]
					target[k] = key
					k -= group

				j += group

		group /= 2

	return target


def bubble_sort(target):
	target = target[:]
	for i in xrange(len(target) - 1):
		changed = False
		for j in xrange(0, len(target) - i - 1):
			if target[j] > target[j + 1]:
				target[j], target[j + 1] = target[j + 1], target[j]
				changed = True

		if not changed:
			break

	return target


print insert_sort(nums)
print shell_sort(nums)
print bubble_sort(nums)


# o(n) ~ o(n^2)
def gnome_sort(target):
	seq = target[:]
	i = 0
	while i < len(seq):
		if i == 0 or seq[i] >= seq[i - 1]:
			i += 1
		else:
			seq[i - 1], seq[i] = seq[i], seq[i - 1]
			i -= 1
	return seq


print gnome_sort(nums)


# o(nlgn), o(n) space
def merge_sort(target):
	seq = target[:]

	mid = (0 + len(seq)) / 2
	left_halves = seq[:mid]
	right_halves = seq[mid:]

	if len(left_halves) > 1:
		left_halves = merge_sort(left_halves)
	if len(right_halves) > 1:
		right_halves = merge_sort(right_halves)

	res = []

	while left_halves and right_halves:
		if left_halves[-1] > right_halves[-1]:
			res.append(left_halves.pop())
		else:
			res.append(right_halves.pop())

	res.reverse()
	return (left_halves or right_halves) + res


print nums, merge_sort(nums)


def counting_sort(target, val_range):
	res = [0] * (val_range[1] - val_range[0] + 1)
	for i in target:
		res[i - 1] += 1
	return [i + 1 for i in range(len(res)) for _ in range(res[i])]


print counting_sort([1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1], [1, 7])


# space for time
def radix_sort(target):
	target = target[:]
	from collections import defaultdict
	mp = defaultdict(list)
	max_value = max(target)

	def get_max_digits(v):
		i = 0
		while v:
			v /= 10
			i += 1
		return i

	def get_nth_digit(v, i):
		return v / 10**i % 10

	max_digits_count = get_max_digits(max_value)

	for i in range(max_digits_count):
		for it in target:
			mp[get_nth_digit(it, i)].append(it)
		target = [_ for k in range(10) for _ in mp[k]]
		mp = defaultdict(list)
	return target


print radix_sort([1, 11, 10, 22, 2, 33, 34, 3, 15, 13, 102, 1111])


def bucket_sort(target):
	buckets, di = [[] for _ in range(int(len(target) ** 0.5))], max(target)
	for i in target:
		buckets[int(round((i * 1.0 / di) * (len(buckets) - 1)))].append(i)
	return [i for bucket in buckets for i in insert_sort(bucket)]


print bucket_sort(nums)


G = {
	'a': {'b', 'c', 'd'},
	'b': {'d'},
	'c': {'d'},
	'd': {}
}


def top_sort(G):
	from collections import defaultdict
	cm, res = defaultdict(int), []
	for node in G:
		for neighbour in G[node]:
			cm[neighbour] += 1
	no_in_degree_nodes = [node for node in G if cm[node] == 0]

	while no_in_degree_nodes:
		n = no_in_degree_nodes.pop()
		res.append(n)
		for neighbour in G[n]:
			cm[neighbour] -= 1
			if cm[neighbour] == 0:
				no_in_degree_nodes.append(neighbour)

	return res


print top_sort(G)







