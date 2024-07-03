def main():
    N = int(input())
    A = [int(a) - 1 for a in input().split()]
    W = [int(w) for w in input().split()]
    res = solve(N, A, W)
    print(res)


def solve(N, A, W):

    # mem[i] := 箱iに残す荷物の重さ
    mem = [0 for _ in range(N)]

    # 動かした合計重量
    res = 0

    # それぞれの荷物について
    for i, a in enumerate(A):

        # 箱が空か軽い荷物が入っている場合
        if mem[a] < W[i]:

            # 入っている荷物は別の箱に移す
            res += mem[a]

            # 荷物iは箱aに入れられる
            mem[a] = W[i]

        # その他の場合(重い荷物が入っている場合)
        else:

            # 荷物i は別の箱に移す
            res += W[i]

    return res


if __name__ == "__main__":
    main()
