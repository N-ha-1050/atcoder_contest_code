def main():
    A = [tuple(map(int, input().split())) for _ in range(3)]
    res = solve(A)
    print("Takahashi" if res else "Aoki")


def solve(A):
    board = [[None for _ in range(3)] for _ in range(3)]

    def get_winner():
        # 高橋くんが勝った→True、青木くんが勝った→False、勝者がいない→None

        # すべてのマスが埋まっている場合
        flg = True
        points = [0, 0]
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    flg = False
                else:
                    points[1 if board[i][j] else 0] += A[i][j]
        if flg:
            return points[0] < points[1]

        # 横一列が埋まっている場合
        for i in range(3):
            if board[i][0] is None:
                continue

            flg = True
            for j in range(1, 3):
                if board[i][0] != board[i][j]:
                    flg = False
            if flg:
                return board[i][0]

        # 縦一列が埋まっている場合
        for j in range(3):
            if board[0][j] is None:
                continue

            flg = True
            for i in range(1, 3):
                if board[0][j] != board[i][j]:
                    flg = False
            if flg:
                return board[0][j]

        # 右下がりの斜めが埋まっている場合
        if board[0][0] is not None:
            flg = True
            for i in range(1, 3):
                j = i
                if board[0][0] != board[i][j]:
                    flg = False
            if flg:
                return board[0][0]

        # 右上がりの斜めが埋まっている場合
        if board[0][2] is not None:
            flg = True
            for i in range(1, 3):
                j = 2 - i
                if board[0][2] != board[i][j]:
                    flg = False
            if flg:
                return board[0][2]

        return None

    def dfs(me=True, depth=0):
        # print("|" * depth, board)

        # 勝者がいる場合
        if (winner := get_winner()) is not None:
            # print("|" * depth, winner)
            return winner

        # 自分が勝てる盤面があるか
        res = False
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = me
                    res = res or dfs(not me, depth + 1) == me
                    board[i][j] = None

        # print("|" * depth, res)
        return me if res else not me

    return dfs()


if __name__ == "__main__":
    main()
