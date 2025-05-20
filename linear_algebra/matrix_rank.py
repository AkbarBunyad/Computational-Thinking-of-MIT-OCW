# a readly available way to compute rank is through np.linalg. Here, we find it through Gaussian Elimination by converting it to RREF form.

def matrix_rank(A):
    rows, cols = len(A), len(A[0])
    if rows == 0 or cols == 0:
        return 0

    # making a copy of the original just in case
    working_matrix = [[A[i][j] for j in range(cols)]
    for i in range(rows)]

    # treating rank as the number of pivot variables, perceived by Gilbert's explanation
    rank = 0

    # processing each column to find pivots
    for col in range(cols):
        # meanwhile looking for a non-zero entry in the column
        pivot_row = None
        for row in range(rank, rows):
            if working_matrix[row][col]!=0:
                pivot_row = row
                break
        
        # if no pivot is found, we head to the next column
        if pivot_row is None:
            continue

        # swapping current row with pivot one
        if pivot_row != rank:
            working_matrix[rank], working_matrix[pivot_row] = working_matrix[pivot_row], working_matrix[rank]
        
        # scaling the row so that pivot becomes 1
        pivot_value = working_matrix[rank][col]
        for j in range(cols):
            working_matrix[rank][j] /= pivot_value
        
        # making all other entries 0 in this column
        for i in range(rows):
            # skipping the pivot row itself and only modifying the rows with non-zero entries in the (pivot) column to avoid redundant operation
            if i != rank and working_matrix[i][col] != 0:
                factor = working_matrix[i][col]
                for j in range(cols):
                    working_matrix[i][j] -= factor * working_matrix[rank][j]
        
        rank+=1

    return rank

if __name__ == "__main__":
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix2 = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ]
    matrix3 = [
        [3, 0, 5],
        [1, 4, 6],
        [0, 3, 7]
    ]
    print("Rank of matrix1:", matrix_rank(matrix1))  # Expected: 2
    print("Rank of matrix2:", matrix_rank(matrix2))  # Expected: 1
    print("Rank of matrix3:", matrix_rank(matrix3))  # Expected: 3

