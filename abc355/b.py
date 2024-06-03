def main():
    N, M = map(int, input().split())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]
    res = solve(N, M, A, B)
    print("Yes" if res else "No")


def solve(N, M, A, B):

    # C[i] := (value, is_a)
    C = sorted([(a, True) for a in A] + [(b, False) for b in B])

    for (c1, is_a1), (c2, is_a2) in zip(C, C[1:]):
        if is_a1 and is_a2:
            return True
    return False


if __name__ == "__main__":
    main()
