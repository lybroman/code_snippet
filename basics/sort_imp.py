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
