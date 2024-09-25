def main():
    N, X, Y = map(int, input().split())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]
    res = solve(N, X, Y, A, B)
    print(res)


def solve(N, X, Y, A, B):

    cnt_a = 0
    res_a = 0
    for a in sorted(A, reverse=True):
        cnt_a += a
        res_a += 1
        if cnt_a > X:
            break

    cnt_b = 0
    res_b = 0
    for b in sorted(B, reverse=True):
        cnt_b += b
        res_b += 1
        if cnt_b > Y:
            break
    return min(res_a, res_b)


if __name__ == "__main__":
    main()
