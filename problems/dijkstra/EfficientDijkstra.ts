// In this file we will implement dijkstra algorithm using customly created priority queue.

class PriorityQueue<T extends [number, number]> {
	values: T[]
	size: number
	constructor() {
		this.values = []
		this.size = 0
	}
	private heapifyUp(lastIndex: number) {
		let parentIdx = Math.floor((lastIndex - 1) / 2)
		let currIdx = lastIndex
		while (currIdx > 0 && this.values[currIdx][0] < this.values[parentIdx][0]) {
			let temp = this.values[currIdx]
			this.values[currIdx] = this.values[parentIdx]
			this.values[parentIdx] = temp

			currIdx = parentIdx
			parentIdx = Math.floor((currIdx - 1) / 2)
		}
	}
	private heapifyDown(index: number) {
		let leftChild = 2 * index + 1
		let rightChild = 2 * index + 2
		let smallest = index
		if (
			leftChild < this.size &&
			this.values[leftChild][0] < this.values[smallest][0]
		) {
			smallest = leftChild
		}
		if (
			rightChild < this.size &&
			this.values[rightChild][0] < this.values[smallest][0]
		) {
			smallest = rightChild
		}

		if (smallest != index) {
			let temp = this.values[index]
			this.values[index] = this.values[smallest]
			this.values[smallest] = temp
			this.heapifyDown(smallest)
		}
	}
	heappush(val: T) {
		this.values.push(val)
		this.size += 1
		this.heapifyUp(this.size - 1)
	}

	heappop() {
		if (this.size == 0) {
			return
		}
		if (this.size == 1) {
			this.size -= 1
			return this.values.pop()
		}

		let root = this.values[0]
		this.values[0] = this.values.pop()!
		this.size -= 1
		this.heapifyDown(0)
		return root
	}

	peek() {
		if (this.size > 0) {
			return this.values[0]
		}
	}
	isEmpty() {
		return this.size == 0
	}
}

class Graph {
	graph: Map<number, Array<Array<number>>>
	size: number
	constructor(edges: Array<Array<number>>, size: number) {
		this.graph = new Map()
		this.size = size
		for (const [x, y, w] of edges) {
			if (!this.graph.has(x)) {
				this.graph.set(x, [])
			}
			this.graph.get(x)!.push([y, w])
		}
	}

	shortestPaths(start: number) {
		let distances = Array(this.size).fill(Number.MAX_VALUE)
		distances[start] = 0
		// [dist, node]
		let minHeap = new PriorityQueue<[number, number]>()
		minHeap.heappush([0, start])
		while (!minHeap.isEmpty()) {
			const [dist, node] = minHeap.heappop()!
			if (dist > distances[node]) {
				continue
			}
			for (const [nei, nei_dist] of this.graph.get(node) || []) {
				const new_dist = dist + nei_dist
				if (new_dist < distances[nei]) {
					distances[nei] = new_dist
					minHeap.heappush([new_dist, nei])
				}
			}
		}
		return distances
	}
}

const graph = new Graph(
	[
		[0, 3, 3],
		[1, 4, 1],
		[1, 2, 1],
		[1, 0, 8],
		[2, 3, 1],
		[4, 0, 2],
	],
	5
)
console.log(graph.shortestPaths(1))
