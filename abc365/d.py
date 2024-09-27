def main():
    N = int(input())
    S = input()
    res = solve(N, S)
    print(res)


def solve(N, S):

    # 出した手を数値に変えるための辞書
    h2n = {"R": 0, "P": 1, "S": 2}

    # judge[青木くんの手][高橋くんの手] := (高橋くんの勝数の増加分、負けたなら None)
    judge = [[0, 1, None], [None, 0, 1], [1, None, 0]]

    # DP(動的計画法)用リスト
    dp = [0, 0, 0]

    for s in S:
        # DP更新用リスト
        ndp = [None, None, None]

        # 青木くんの手を数値に変える
        n = h2n[s]

        # 高橋くんの出す手を3通り試す
        for i, j in enumerate(judge[n]):
            if j is None:
                # 高橋くんが負けたなら次へ
                continue

            # 新しい値を計算
            # d is not None: 一つ前で手kを出すことが可能
            # k != i: 同じ手を連続しない
            ndp[i] = max(d for k, d in enumerate(dp) if d is not None and k != i) + j

        # DP用リストを更新
        dp = ndp

    return max(d for d in dp if d is not None)


if __name__ == "__main__":
    main()
