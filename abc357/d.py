def main():
    N = int(input())
    res = solve(N)
    print(res)


def solve(N):
    MOD = 998244353

    # N の桁数を求める
    M = len(str(N))

    # N * (10 ** (M * N) - 1) / (10 ** M - 1) をMODを取りながら求める

    # N
    a = N % MOD

    # 10 ** (M * N) - 1
    # pow関数を使うと効率よくMODを取った累乗を求められる
    # (内部で繰り返し二乗法が実装されている)
    b = pow(10, M * N, MOD) - 1
    b %= MOD

    # 1 / (10 ** M - 1)
    # pow関数の第二引数に-1を入れると逆数も求められる
    # (内部でフェルマーの小定理が実装されている)
    c = pow(pow(10, M, MOD) - 1, -1, MOD)

    res = a * b
    res %= MOD
    res *= c
    res %= MOD

    return res


# 愚直解
def solve_gu(N):
    MOD = 998244353

    M = len(str(N))
    pow_10_M = 10**M

    res = 0
    for i in range(N):
        res += N * (pow_10_M**i)
        res %= MOD
    return res


if __name__ == "__main__":
    main()
