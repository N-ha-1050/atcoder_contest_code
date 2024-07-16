def main():
    N = int(input())
    LR = [tuple(map(int, input().split())) for _ in range(N)]
    L, R = zip(*LR)
    res = solve(N, L, R)
    if res is None:
        print("No")
    else:
        print("Yes")
        print(*res)


def solve(N, L, R):
    sum_L = sum(L)
    sum_R = sum(R)

    # 作成不可能な場合
    if not (sum_L <= 0 <= sum_R):
        return None

    # Lで初期化
    X = [x for x in L]

    # 不足分を正の値で管理
    gap = -sum_L

    # すでに条件を満たしている場合
    if gap == 0:
        return X

    for i in range(N):

        # X[i] を更新
        diff = min(gap, R[i] - L[i])
        X[i] += diff
        gap -= diff

        # 作成できた場合
        if gap == 0:
            return X


if __name__ == "__main__":
    main()
