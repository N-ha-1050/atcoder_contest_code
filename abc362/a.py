def main():
    R, G, B = map(int, input().split())
    C = input()
    res = solve(R, G, B, C)
    print(res)


def solve(R, G, B, C):
    if C == "Red":
        print(min(G, B))
    if C == "Green":
        print(min(B, R))
    if C == "Blue":
        print(min(R, G))


if __name__ == "__main__":
    main()
