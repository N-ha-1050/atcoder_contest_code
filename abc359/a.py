def main():
    N = int(input())
    S = [input() for _ in range(N)]
    res = solve(N, S)
    print(res)


def solve(N, S):
    return S.count("Takahashi")


if __name__ == "__main__":
    main()
