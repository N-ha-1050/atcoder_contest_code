def main():
    N, T = map(int, input().split())
    A = [int(a) - 1 for a in input().split()]
    res = solve(N, T, A)
    print(res)


def solve(N, T, A):
    # 行と列のカウント
    cnt_h, cnt_v = [0 for _ in range(N)], [0 for _ in range(N)]

    # 右下がりと右上がりの斜めのカウント
    cnt_rd, cnt_ru = 0, 0

    for turn, a in enumerate(A, 1):
        # a を 行と列に変換
        i, j = a // N, a % N

        # i行目の更新
        cnt_h[i] += 1
        if cnt_h[i] == N:
            return turn

        # j列目の更新
        cnt_v[j] += 1
        if cnt_v[j] == N:
            return turn

        # 右下がりの更新
        if i == j:
            cnt_rd += 1
            if cnt_rd == N:
                return turn

        # 右上がりの更新
        if i == (N - j - 1):
            cnt_ru += 1
            if cnt_ru == N:
                return turn
    return -1


if __name__ == "__main__":
    main()
