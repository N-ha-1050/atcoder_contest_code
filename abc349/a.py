def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    res = solve(N, A)
    print(res)


def solve(N, A):
    res = -sum(A)
    return res


if __name__ == "__main__":
    main()
