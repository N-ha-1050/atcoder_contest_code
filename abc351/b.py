def main():
    N = int(input())
    A = [input() for _ in range(N)]
    B = [input() for _ in range(N)]
    res = solve(N, A, B)
    print(*res)


def solve(N, A, B):
    for i in range(N):
        for j in range(N):
            if A[i][j] != B[i][j]:
                return (i + 1, j + 1)


if __name__ == "__main__":
    main()
