def main():
    N, M = map(int, input().split())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]
    res = solve(N, M, A, B)
    print(res)


def solve(N, M, A, B):

    # 箱を少ない順に並べる
    sorted_A = sorted(A)

    # 箱のインデックス
    idx = 0

    # 合計金額
    res = 0

    # 少なくていい人から順に見る
    for b in sorted(B):

        # 現在の箱に入っている個数がbよりも少なければ、見る箱を一つ次へ
        while idx < N and sorted_A[idx] < b:
            idx += 1

        # すべての箱を見終えたら、b個のお菓子はあげられないということなので-1
        if idx >= N:
            return -1

        # idx番目の箱を選択するので、合計金額に加える
        res += sorted_A[idx]

        # 次の箱へ進める
        idx += 1

    return res


if __name__ == "__main__":
    main()
