def main():
    N = int(input())
    H = [int(h) for h in input().split()]
    res = solve(N, H)
    print(res)


def solve(N, H):
    for i, h in enumerate(H[1:], 2):
        if h > H[0]:
            return i
    return -1


if __name__ == "__main__":
    main()
