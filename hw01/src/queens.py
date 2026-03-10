def solve_n_queens(n):
    """
    使用回溯法求解N皇后问题
    返回所有可能的解
    """
    def is_safe(board, row, col):
        """检查在(row, col)位置放置皇后是否安全"""
        # 检查同一列
        for i in range(row):
            if board[i] == col:
                return False
        
        # 检查左上对角线
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i] == j:
                return False
        
        # 检查右上对角线
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i] == j:
                return False
        
        return True
    
    def backtrack(row):
        """回溯函数，尝试在第row行放置皇后"""
        if row == n:
            # 找到一个解，保存结果
            solution = []
            for i in range(n):
                line = ['.' for _ in range(n)]
                line[board[i]] = 'Q'
                solution.append(''.join(line))
            solutions.append(solution)
            return
        
        # 尝试在当前行的每一列放置皇后
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col  # 放置皇后
                backtrack(row + 1)  # 递归处理下一行
                board[row] = -1  # 回溯，撤销选择
    
    solutions = []
    board = [-1] * n  # board[i]表示第i行皇后所在的列
    backtrack(0)
    return solutions


def print_solutions(solutions):
    """打印所有解"""
    if not solutions:
        print("无解")
        return
    
    print(f"共找到 {len(solutions)} 个解\n")
    
    for idx, solution in enumerate(solutions, 1):
        print(f"解 {idx}:")
        for line in solution:
            print(line)
        print()


def solve_n_queens_count(n):
    """
    只计算解的数量，不保存具体解（更节省内存）
    """
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col:
                return False
            if abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    
    count = 0
    board = [-1] * n
    backtrack(0)
    return count


if __name__ == "__main__":
    # 测试4皇后问题
    print("=" * 40)
    print("4皇后问题")
    print("=" * 40)
    solutions = solve_n_queens(4)
    print_solutions(solutions)
    
    # 测试8皇后问题（只显示解的数量）
    print("=" * 40)
    print("8皇后问题")
    print("=" * 40)
    count = solve_n_queens_count(8)
    print(f"8皇后问题共有 {count} 个解")
    
    # 测试其他规模的N皇后问题
    print("\n" + "=" * 40)
    print("不同规模的N皇后问题解的数量")
    print("=" * 40)
    for n in range(1, 11):
        count = solve_n_queens_count(n)
        print(f"{n}皇后: {count} 个解")
