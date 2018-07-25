class Solution(object):
	def carFleet(self, target, position, speed):
		if not position or not speed or len(position) != len(speed):
			return 0

		durations = sorted([(float(target - p) / s, p, s) for p, s in zip(position, speed)], reverse=True)

		count = 1
		cur_duration = durations[0][0]
		cur_p = durations[0][1]
		for d, p, s in durations:
			if d == cur_duration:
				continue
			elif p < cur_p:
				continue
			else:
				cur_duration = d
				cur_p = p
				count += 1

		return count


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print Solution().carFleet(target, position, speed)