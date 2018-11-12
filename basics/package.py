def package_01(obj_list, package_size):
	obj_num = len(obj_list)
	data = [[0] * (package_size + 1) for _ in xrange(obj_num)]
	for j in xrange(package_size + 1):
		for i in xrange(obj_num):
			if i > 0:
				data[i][j] = data[i - 1][j]
			if j >= obj_list[i]:
				max_without_i = data[i - 1][j - obj_list[i]] if i > 0 else 0
				data[i][j] = max(data[i][j], max_without_i + obj_list[i])

	print data
	return data[obj_num - 1][package_size]


def main():
	jobs = [1, 3, 4, 5, 6, 2]
	jobs.sort()

	jobs_sum = sum(jobs)
	aim = jobs_sum / 2

	res = package_01(jobs, aim)
	print jobs_sum - res


if __name__ == '__main__':
	main()
