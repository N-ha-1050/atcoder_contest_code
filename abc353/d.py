def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    res = solve(N, A)
    print(res)


def solve(N, A):
    MOD = 998244353

    # 各値の桁数を記録
    dig_A = [len(str(a)) for a in A]

    # それぞれの桁数の数がいくつあるか記録
    cnt = [0 for _ in range(max(dig_A) + 1)]
    for dig_a in dig_A:
        cnt[dig_a] += 1

    res = 0
    for i, a in enumerate(A):

        # 自分の分を減らす
        cnt[dig_A[i]] -= 1

        # 自分より前の値と足すときは自分はそのまま
        res += a * i
        res %= MOD

        # cnt に残っているのは自分より後ろの値の情報
        # 自分より後ろの値と足すときは自分を 10^dig 倍する
        # (一応毎回MOD取っているけど、Pythonは割と適当にMODをとっても大丈夫)
        for dig, n in enumerate(cnt):
            res += a * pow(10, dig, MOD) * n
            res %= MOD

    return res


if __name__ == "__main__":
    main()
