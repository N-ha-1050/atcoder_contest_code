def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    res = solve(N, A)
    print(res)


def solve(N, A):
    MOD = 998244353

    # 自分より前の総和
    cnt = 0

    res = 0

    for i, a in enumerate(A):

        # 自分が後ろのとき
        res += a * i
        res %= MOD

        # 自分が前のとき
        res += pow(10, len(str(a)), MOD) * cnt
        res %= MOD

        cnt += a

    return res


if __name__ == "__main__":
    main()
