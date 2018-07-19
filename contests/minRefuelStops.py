class Solution(object):
	def minRefuelStops(self, target, startFuel, stations):
		max_distance =[startFuel for _ in range(len(stations) + 1)]

		for i in range(0, len(stations)):
			for j in range(i + 1, 0, -1):
				if max_distance[j - 1] >= stations[i][0]:
					max_distance[j] = max(max_distance[j], max_distance[j - 1] + stations[i][1])

		for j in range(0, len(stations) + 1):
			if max_distance[j] >= target:
				return j

		return -1


class Solution1(object):
	def minRefuelStops(self, target, startFuel, stations):
		import Queue
		pq = Queue.PriorityQueue()
		max_distance = startFuel
		at_stop = 0
		total_stops = len(stations)
		stops = 0
		while True:
			if max_distance >= target:
				return stops

			while at_stop < total_stops and max_distance >= stations[at_stop][0]:
				pq.put(stations[at_stop][1] * -1)
				at_stop += 1

			if pq.empty(): return -1
			max_distance += pq.get() * -1
			stops += 1


print Solution().minRefuelStops(1000, 83, [[25,27],[36,187],[140,186],[378,6],[492,202],[517,89],[579,234],[673,86],[808,53],[954,49]])
print Solution1().minRefuelStops(100, 50, [[25,25],[50,50]])