def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    res = solve(N, A)
    print(res)


def solve(N, A):
    cnt = 0

    # 一つ飛ばしのペアを全探索
    for i in range(2 * N - 2):
        if A[i] == A[i + 2]:
            cnt += 1
    return cnt


if __name__ == "__main__":
    main()
