def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    res = solve(N, A)
    print(res)


def solve(N, A):
    MOD = 998244353

    # 何倍すればよいのか記録
    cnt = N

    res = 0

    # 後ろから見ていく
    for a in A[::-1]:

        # 後ろにつく自分の分を減らす
        cnt -= 1

        # cnt 倍して加える
        res += a * cnt
        res %= MOD

        # 前につく自分の分を追加
        cnt += pow(10, len(str(a)), MOD)
        cnt %= MOD

    return res


if __name__ == "__main__":
    main()
