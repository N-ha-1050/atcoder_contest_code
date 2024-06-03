def main():
    N = int(input())
    SC = [input().split() for _ in range(N)]
    S, C_ = zip(*SC)
    C = [int(c) for c in C_]
    res = solve(N, S, C)
    print(res)


def solve(N, S, C):
    return sorted(S)[sum(C) % N]


if __name__ == "__main__":
    main()
