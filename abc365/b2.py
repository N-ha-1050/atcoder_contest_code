def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    res = solve(N, A)
    print(res)


def solve(N, A):
    return sorted(range(N), key=lambda x: A[x], reverse=True)[1] + 1


if __name__ == "__main__":
    main()
