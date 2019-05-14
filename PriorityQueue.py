from math import floor
class PriorityQueue:
	def __init__(self):
		self.q = [0]

	def enqueue(self, value):
		self.q.append(value)
		self.bubbleUp(self.q)

	def bubbleUp(self, q):
		parent = len(q) - 1
		self._bubbleUp(q, parent)

	def _bubbleUp(self,q, index):
		if index == 0:
			return
		else:
			if q[index] < q[floor(index/2)]:
				q[index], q[floor(index/2)] = q[floor(index/2)], q[index]
				self._bubbleUp(q, floor(index/2))

	def dequeue(self):
		value = self.q[1]
		self.q[1], self.q[-1] = self.q[-1], self.q[1]
		self.q = self.q[:-1]
		self.bubbleDown(self.q, 1)
		return value

	def bubbleDown(self, q, index):
		leftIndex = index * 2
		rightIndex = index * 2 + 1
		if(index >= len(self.q)):
			return
		if leftIndex  < len(self.q) and self.q[index] > self.q[leftIndex]:
			self.q[index] , self.q[leftIndex] = self.q[leftIndex] , self.q[index]
			self.bubbleDown(self.q, leftIndex)
		if rightIndex  < len(self.q) and self.q[index] > self.q[rightIndex]:
			self.q[index] , self.q[rightIndex] = self.q[rightIndex] , self.q[index]
			self.bubbleDown(self.q, rightIndex)

	def peek(self):
		if len(self.q) > 1:
			return self.q[1]
		else:
			return "The queue is empty"

	def __len__(self):
		return len(self.q)

q = PriorityQueue()

data = [1/2,0.414,3/4,4/5,5/6,9.9]

result = []

for i in data:
	q.enqueue(i)

while len(q) > 1:
	result.append(q.dequeue())

print(data)
print(result)
