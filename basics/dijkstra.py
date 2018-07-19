import heapq
from collections import defaultdict


def dijkstra_dist_graph(edges, source):
	graph = defaultdict(list)

	for src, dest, weight in edges:
		graph[src].append((weight, dest))

	queue = [(0, source)]
	nodes = set()
	dists = {source: 0}

	while queue:
		print queue, nodes
		dist, node = heapq.heappop(queue)

		if node not in nodes:
			nodes.add(node)
		else:
			continue

		for weight, dest in graph[node]:

			if dest in nodes:
				continue

			prev_min_dist = dists.get(dest, None)
			cur_dist = dist + weight

			if not prev_min_dist or cur_dist < prev_min_dist:
				dists[dest] = cur_dist
				heapq.heappush(queue, (cur_dist, dest))

	return dists


def dijkstra_min_dist(edges, source, destination):

	graph = defaultdict(list)

	for src, dest, weight in edges:
		graph[src].append((weight, dest))

	nodes = set()
	queue = [(0, source, "")]
	dists = {source: 0}

	while queue:
		dist, node, path = heapq.heappop(queue)

		path = path + node

		if node == destination:
			return dist, path

		if node not in nodes:
			nodes.add(node)
		else:
			continue

		for weight, dest in graph[node]:

			if dest in nodes:
				continue

			prev_min_dist = dists.get(dest, None)
			cur_dist = dist + weight

			if not prev_min_dist or prev_min_dist > cur_dist:
				dists[dest] = cur_dist
				heapq.heappush(queue, (cur_dist, dest, path))

	return -1, ()


def dijkstra_multi_nodes_dist_graph(edges, source, target_nodes):

	graph = defaultdict(list)

	for src, dest, weight in edges:
		graph[src].append((weight, dest))

	nodes = set()
	queue = [(0, (source, source), "")]
	dists = {(source, source): 0}

	while queue:
		dist, node, path = heapq.heappop(queue)

		if node in nodes:
			continue
		else:
			nodes.add(node)

		path += node[0]

		if target_nodes.issubset(set(node[1])):
			return dist, path

		for weight, dest in graph[node[0]]:
			dest = (dest, ''.join(set(node[1] + dest)))

			if dest in nodes:
				continue

			prev_min_dist = dists.get(dest, None)
			cur_dist = dist + weight
			#print dest, prev_min_dist, cur_dist
			if not prev_min_dist or cur_dist < prev_min_dist:
				dists[dest] = cur_dist
				heapq.heappush(queue, (cur_dist, dest, path))
		#print queue, nodes

	print dists

	return -1, ""


if __name__ == "__main__":
	edges = [
		("A", "B", 7),
		("A", "D", 5),
		("B", "C", 8),
		("B", "D", 99),
		("B", "E", 9),
		("C", "E", 5),
		("D", "E", 15),
		("D", "F", 6),
		("E", "F", 8),
		("E", "G", 9),
		("F", "G", 11)
	]

	print "=== Dijkstra Distance Graph==="
	#print dijkstra_dist_graph(edges, "A")

	print "=== Dijkstra Min Distance==="
	print dijkstra_min_dist(edges, "A", "E")

	print "=== Dijkstra Multi Nodes Min Distance==="
	print dijkstra_multi_nodes_dist_graph(edges, "A", {"A", "G"})

