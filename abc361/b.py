def main():
    C1 = list(map(int, input().split()))
    C2 = list(map(int, input().split()))
    res = solve(C1, C2)
    print("Yes" if res else "No")


def solve(C1, C2):
    # 一般に閉区間[s1, e1]と[s2, e2]に共通区間があることの判定は max(s1, s2) <= min(e1, e2) でできる
    return (
        max(C1[0], C2[0]) < min(C1[3], C2[3])
        and max(C1[1], C2[1]) < min(C1[4], C2[4])
        and max(C1[2], C2[2]) < min(C1[5], C2[5])
    )


if __name__ == "__main__":
    main()
