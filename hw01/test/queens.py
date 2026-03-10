def solve_n_queens(n):
    """求解N皇后问题，返回所有解的数量"""
    def is_safe(board, row, col):
        # 检查同一列
        for i in range(row):
            if board[i] == col:
                return False
        # 检查左上对角线
        for i in range(row):
            if board[i] == col - (row - i):
                return False
        # 检查右上对角线
        for i in range(row):
            if board[i] == col + (row - i):
                return False
        return True

    def backtrack(row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                count += backtrack(row + 1)
                board[row] = -1
        return count

    board = [-1] * n
    return backtrack(0)


def solve_n_queens_with_solutions(n):
    """求解N皇后问题，返回所有解的详细布局"""
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col:
                return False
            if board[i] == col - (row - i):
                return False
            if board[i] == col + (row - i):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions


def print_solution(board, n):
    """打印一个解的棋盘布局"""
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()


if __name__ == "__main__":
    # 验证 N=4 的解数量
    print("=" * 50)
    print("验证 N=4 的八皇后问题")
    print("=" * 50)
    n4_solutions = solve_n_queens_with_solutions(4)
    print(f"N=4 的解数量: {len(n4_solutions)}")
    print(f"\n所有解的详细布局:")
    for i, sol in enumerate(n4_solutions, 1):
        print(f"\n解 {i}:")
        print_solution(sol, 4)

    # 验证 N=8 的解数量
    print("=" * 50)
    print("验证 N=8 的八皇后问题")
    print("=" * 50)
    n8_count = solve_n_queens(8)
    print(f"N=8 的解数量: {n8_count}")
