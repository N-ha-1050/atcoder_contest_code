def main():
    R, G, B = map(int, input().split())
    C = input()
    res = solve(R, G, B, C)
    print(res)


def solve(R, G, B, C):
    match C:
        case "Red":
            return min(G, B)
        case "Green":
            return min(R, B)
        case "Blue":
            return min(R, G)


if __name__ == "__main__":
    main()
