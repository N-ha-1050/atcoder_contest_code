def main():
    R, G, B = map(int, input().split())
    C = input()
    res = solve(R, G, B, C)
    print(res)


def solve(R, G, B, C):
    cnt = {"Red": R, "Green": G, "Blue": B}
    cnt[C] = float("inf")  # 101 とかでもOK
    return min(cnt.values())


if __name__ == "__main__":
    main()
