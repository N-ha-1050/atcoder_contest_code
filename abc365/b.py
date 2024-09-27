def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    res = solve(N, A)
    print(res)


def solve(N, A):
    # 二番目に大きな値を求める
    target = sorted(A, reverse=True)[1]

    # その値のインデックスを返す
    # 注意: .index() は毎回すべての値を見るのでくり返し使わない
    return A.index(target) + 1


if __name__ == "__main__":
    main()
