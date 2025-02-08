def main():
    N, M = map(int, input().split())
    A = [int(a) - 1 for a in input().split()]
    res = solve(N, M, A)
    print(len(res))
    print(*res)


def solve(N: int, M: int, A: list[int]):
    mem = [False for _ in range(N)]
    for a in A:
        mem[a] = True
    return [i + 1 for i in range(N) if not mem[i]]


if __name__ == "__main__":
    main()
