def main():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    res = solve(N, AB)
    # print("Aoki" if res else "Takahashi")
    print("Takahashi" if res else "Aoki")


def solve(N, AB):
    # dp[field] := field で先手が必勝か
    dp = [None for _ in range(1 << N)]

    # カードがないとき先手が負ける
    dp[0] = False

    for field in range(1, 1 << N):
        dp[field] = False
        for i in range(N):
            if not field >> i & 1:
                continue
            for j in range(i + 1, N):
                if not field >> j & 1:
                    continue
                if AB[i][0] == AB[j][0] or AB[i][1] == AB[j][1]:

                    # 1つ進んだ状態で先手が負けるなら、現在は先手必勝
                    if not dp[field ^ (1 << i) ^ (1 << j)]:
                        dp[field] = True

                        # 一個でも True になった(=先手必勝になる方法が見つかった)ならその field は決定
                        break
            else:
                continue
            break

    return dp[(1 << N) - 1]


if __name__ == "__main__":
    main()
