def main():
    N = int(input())
    A = [int(a) - 1 for a in input().split()]
    res = solve(N, A)
    print(len(res))
    for i, j in res:
        print(i + 1, j + 1)


def solve(N, A):
    res = []

    for i in range(N):
        while A[i] != i:
            j = A[i]
            A[i], A[j] = A[j], A[i]

            res.append((i, j))
    return res


if __name__ == "__main__":
    main()
