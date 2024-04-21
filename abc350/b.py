def main():
    N, Q = map(int, input().split())
    T = [int(t) - 1 for t in input().split()]
    res = solve(N, Q, T)
    print(res)


def solve(N, Q, T):
    # 歯が生えていれば True
    mem = [True for _ in range(N)]

    for t in T:
        mem[t] = not mem[t]

    res = sum(mem)
    return mem


if __name__ == "__main__":
    main()
