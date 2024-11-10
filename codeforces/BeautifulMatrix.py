def find_min_moves(matrix):
    
    current_row = current_col = None
    
    
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                current_row, current_col = i, j
                break
        if current_row is not None:
            break
    
   
    target_row, target_col = 2, 2
    
    
    min_moves = abs(current_row - target_row) + abs(current_col - target_col)
    
    return min_moves


matrix = []
for _ in range(5):
    row = list(map(int, input().strip().split()))
    matrix.append(row)


print(find_min_moves(matrix))