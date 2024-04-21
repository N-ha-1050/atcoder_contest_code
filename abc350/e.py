def main():
    N, A, X, Y = map(int, input().split())
    res = solve(N, A, X, Y)
    print(res)


def solve(N, A, X, Y):
    mem = {0: 0}

    def calc(x=N):
        if x in mem:
            return mem[x]
        res1 = calc(x // A) + X
        res2 = (sum(calc(x // i) for i in range(2, 7)) + Y * 6) / 5
        mem[x] = min(res1, res2)
        return mem[x]

    res = calc()
    return res


if __name__ == "__main__":
    main()
