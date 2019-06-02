def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    for i in range(len(board)):
      for j in range(len(board[0])):
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        if board[i][j] == word[0]:
          visited[i][j] = True
          if self._board(board, word[1:], visited, i, j):
            return True
    return False

def _board(self, board, word, visited, i, j):

  if word == '':
    return True
  direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]

  for d in direction:
    i += d[0]
    j += d[1]

    if i in range(0, len(board)) and j in range(0, len(board[0])):
      if board[i][j] == word[0] and visited[i][j] == False:
        visited[i][j] = True
        if self._board(board, word[1:], visited, i, j):
          return True
        visited[i][j] = False
    i -= d[0]
    j -= d[1]

  return False
