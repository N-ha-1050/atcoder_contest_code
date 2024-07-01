def main():
    N = int(input())
    res = solve(N)
    for r in res:
        print("".join(r))


def solve(N):

    # mem[k][i][j] := レベルkのカーペットのi行目j列目の値
    mem = [[[None for _ in range(3**k)] for _ in range(3**k)] for k in range(N + 1)]

    # レベル0を定義
    mem[0] = [["#"]]

    # レベルが小さい順に作っていく
    for k in range(N):

        # レベル k + 1 を作る
        for i in range(3 ** (k + 1)):
            for j in range(3 ** (k + 1)):

                # 中央のブロックの場合
                if i // (3**k) == 1 and j // (3**k) == 1:
                    mem[k + 1][i][j] = "."

                # 他のブロックの場合
                else:
                    mem[k + 1][i][j] = mem[k][i % (3**k)][j % (3**k)]

    # レベルNを返す
    return mem[N]


if __name__ == "__main__":
    main()
