'''
You are asked to cut off trees in a forest for a golf event.
The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through,
and this positive number represents the tree's height.

You are asked to cut off all the trees in this forest in the order of
tree's height - always cut off the tree with lowest height first.
And after cutting, the original place has the tree will become
a grass (value 1).

You will start from the point (0, 0) and
you should output the minimum steps you need to walk to cut off all the trees.
If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height
and there is at least one tree needs to be cut off.

Input:
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6

'''
def cutOffTree(self, forest):
    """
    :type forest: List[List[int]]
    :rtype: int
    """
    height = []

    for i in range(len(forest)):
        for j in range(len(forest[0])):
            if forest[i][j] > 0:
                height.append([forest[i][j], i, j])
    height.sort()

    totalSteps = 0

    si = 0
    sj = 0

    for i in height:
        ti = i[1]
        tj = i[2]
        steps = self.BFS(forest, si, sj, ti, tj)
        if steps == float('inf'):
          return -1
        forest[ti][tj] = 1
        totalSteps += steps
        si = ti
        sj = tj

    if totalSteps == float('inf'):
      return -1

    return totalSteps
def BFS(self, forest, si, sj, ti, tj):

  distance = 0
  visited = [[False] * len(forest[0]) for _ in range(len(forest))]

  nodeBuffer = []
  nodeBuffer.append([si, sj])
  visited[si][sj] = True

  while len(nodeBuffer):
    nextLeveBuffer = []
    for i in nodeBuffer:
      ci = i[0]
      cj = i[1]
      if ci == ti and cj == tj:
        return distance
      if ci - 1 >= 0 and forest[ci - 1][cj] > 0 and visited[ci - 1][cj] == False:
        nextLeveBuffer.append([ci - 1, cj])
        visited[ci - 1][cj] = True
      if cj - 1 >= 0 and forest[ci][cj - 1] > 0 and visited[ci][cj - 1] == False:
        nextLeveBuffer.append([ci, cj - 1])
        visited[ci][cj - 1] = True
      if ci + 1 < len(forest) and forest[ci + 1][cj] > 0 and visited[ci + 1][cj] == False:
        nextLeveBuffer.append([ci + 1, cj])
        visited[ci + 1][cj] = True
      if cj + 1 < len(forest[0]) and forest[ci][cj + 1] > 0 and visited[ci][cj + 1] == False:
        nextLeveBuffer.append([ci, cj + 1])
        visited[ci][cj + 1] = True
    nodeBuffer = nextLeveBuffer
    distance += 1
  return float('inf')
