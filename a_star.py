import copy 

def process_input_file(file_path="input.txt"):  # 3,0   7,2   2,6
    data = []
    with open(file_path, 'r') as f:
        data = f.readlines()
    assert len(data) == 2
    print(int(data[0].strip()))
    queens = data[1].replace(')', '')
    queens = queens.replace('(', '')
    queens = queens.replace(', ', ',')
    queens = queens.split(' ')
    for i in range(len(queens)):
        queens[i] = queens[i].split(',')
        queens[i] = list(map(int, queens[i]))
        queens[i] = tuple(queens[i])
    print(queens)
    return queens

N = 8
initQueen = process_input_file()

def cnf_col( row, col):
  list_col = []
  for i in range(N):
    if i != row:
      list_col.append((i, col))
  return list_col

def cnf_row( row, col):
  list_row = []
  for i in range(N):
    if i != col:
      list_row.append((row, i))
  
  return list_row

def check_in_range(n):
  if (n > N-1 or n < 0) :
    return False
  return True # 0 <= n <= N-1

def cnf_diagonal( row, col):
  list_diagonal = []
  
  check_row, check_col = row - 1, col - 1
  while check_in_range(check_row) and check_in_range(check_col):
    list_diagonal.append((check_row, check_col))
    check_row -= 1
    check_col -= 1
  
  check_row, check_col = row + 1, col + 1
  while check_in_range(check_row) and check_in_range(check_col):
    list_diagonal.append((check_row, check_col))
    check_row += 1
    check_col += 1

  check_row, check_col = row + 1, col - 1
  while check_in_range(check_row) and check_in_range(check_col):
    list_diagonal.append((check_row, check_col))
    check_row += 1
    check_col -= 1

  check_row, check_col = row - 1, col + 1
  while check_in_range(check_row) and check_in_range(check_col):
    list_diagonal.append((check_row, check_col))
    check_row -= 1
    check_col += 1

  return list_diagonal
  

def initboard(N, initQueen, need_placed_queens):
    board = []
    for i in range(N):
        subboard = []
        for j in range(N):
            subboard.append(0)
        board.append(subboard)
    
    for queen in initQueen:
        row, col = queen
        board[row][col] = 1
    
    for queen in need_placed_queens:
        row, col = queen
        board[row][col] = 1
    
    return board

def calculate_attack_queens(current_queen, other_queens):
    count = 0
    cnfs = cnf_col(current_queen[0], current_queen[1]) + cnf_row(current_queen[0], current_queen[1]) + cnf_diagonal(current_queen[0], current_queen[1])
    for queen in other_queens:
        for cnf in cnfs:
            if cnf[0] == queen[0] and cnf[1] == queen[1]:
                count += 1
    
    return count # 0 <= c <= 7 , it can attack at least 1 and max 7

def pairs_attack(board):
    counts = 0
    current_queens = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                current_queens.append((i, j))
    assert len(current_queens) == N
    for i in range(len(current_queens)):
        count = calculate_attack_queens(current_queens[i], current_queens[i+1:])
        counts = counts + count
    return counts

def check_can_place(queen, right_queens, need_placed_queens_temp = [] ):
    count = calculate_attack_queens(queen, right_queens)
    count1 = calculate_attack_queens(queen, need_placed_queens_temp)
    if count == 0 and count1 == 0:
       return True
    return False

def check_place_in_col(i, j, right_queens):
    for queen in right_queens:
        if j == queen[1]:
            return False
    return True

def transform_to_heuristic(priority_queue):
    A = copy.deepcopy(priority_queue)

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i][1] + A[i][2] > A[j][1] + A[j][2]:
                A[i], A[j] = A[j], A[i]
    # sort here
    return A

import numpy as np

def print_q(queue):
    for q in queue:
        (a,b,c,d) = q
        print(np.array(a))
        print("g = ", b)
        print("h = ", c)
        print("needed to place = ", d)

def solveNQueen():
    right_placed_queens = []
    need_placed_queens = []

    visited_board = [] # if visited, ignore

    for queen in initQueen:
        right_placed_queens.append(queen)
    
    for i in range(N):
        for j in range(N):
            if (i, j) not in initQueen and check_place_in_col(i, j, initQueen):
                need_placed_queens.append((i, j))

            if len(need_placed_queens) == N - len(right_placed_queens):
                    break
        if len(need_placed_queens) == N - len(right_placed_queens):
                    break

    board = initboard(N, right_placed_queens, need_placed_queens)

    priority_queue = []  # list of state of board, used to sort and get least cost state, f = g + h
    priority_queue.append((board, 0, pairs_attack(board), need_placed_queens)) # (board, g, h, queens needed to place)

    assert len(right_placed_queens) + len(need_placed_queens) == N
    
    print("start")
    k = 0
    while priority_queue:
        print("k = ",k)

        priority_queue = transform_to_heuristic(priority_queue)
        #print_q(priority_queue)
        
        (board, g, h, need_placed_queens) = priority_queue.pop(0)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(np.array(board))
        print(g, h, need_placed_queens)


        if (board, g, h, need_placed_queens) not in visited_board:
            visited_board.append((board, g, h, need_placed_queens))
            assert h == pairs_attack(board)
            if h == 0:
                print("COMPLETE")
                print(np.array(board))
                return visited_board
            
            (r, c) = need_placed_queens[k]
    
            for i in range(N):
                need_placed_queens_temp = copy.deepcopy(need_placed_queens)
                   
                if check_can_place((i,c), right_placed_queens, need_placed_queens_temp[:k]):
                    need_placed_queens_temp[k] = (i, c)
                            
                    board_temp = initboard(N, right_placed_queens, need_placed_queens_temp)
                    if (board_temp, g + 1,pairs_attack(board_temp), need_placed_queens_temp)  not in visited_board :
                        priority_queue.append((board_temp, g + 1, pairs_attack(board_temp), need_placed_queens_temp))
        
        print("length", len(priority_queue))
        if k == N - len(right_placed_queens) - 1:
            k = 0
            (r, c) = need_placed_queens[k]
            print(r, c)
            
            for queen_state in priority_queue:
                (state, g, h, placed) = queen_state
                if state[r][c] == 1:
                    priority_queue.remove(queen_state)
        else:
            k = k + 1
        print("k-validate = ", k)
    return visited_board

visited_boards = solveNQueen()

print_q(visited_boards)

import matplotlib.pyplot as plt
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

fig, ax = plt.subplots()

im = ax.imshow(visited_boards[len(visited_boards) - 1][0])

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(labels)), labels=labels)
ax.set_yticks(np.arange(len(labels)), labels=labels)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

ax.set_title("Chess board, yellow cells are Queens ")
fig.tight_layout()
plt.show()