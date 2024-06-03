def main():
    N, M = map(int, input().split())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]
    res = solve(N, M, A, B)
    print("Yes" if res else "No")


def solve(N, M, A, B):

    C = sorted(A + B)

    for c1, c2 in zip(C, C[1:]):
        if c1 in A and c2 in A:
            return True
    return False


if __name__ == "__main__":
    main()
