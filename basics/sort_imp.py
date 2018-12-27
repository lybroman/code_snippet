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










