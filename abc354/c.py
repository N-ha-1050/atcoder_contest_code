def main():
    N = int(input())
    AC = [tuple(map(int, input().split())) for _ in range(N)]
    res = solve(N, AC)
    print(len(res))
    print(*res)


def solve(N, AC):

    # AC を C でソートする
    # sorted_AC[i] := (idx, (A[idx], C[idx]))
    # i番目にコストが小さいカードは カードidx で、強さは A[idx] 、コストは C[idx]

    sorted_AC = sorted(enumerate(AC, 1), key=lambda x: x[1][1])

    # 現在の最大値を記録
    ma = 0

    res = set()
    for idx, (a, c) in sorted_AC:

        # これまでの最大値よりも大きいとき
        if ma < a:
            # 答えに追加して、最大値を更新
            res.add(idx)
            ma = a

    return sorted(res)


if __name__ == "__main__":
    main()
