def main():
    S = input()
    T = input()
    res = solve(S, T)
    print("Yes" if res else "No")


def solve(S, T):
    # T を小文字にしておく
    t = T.lower()

    # S の末尾に x を追加
    S += "x"

    # インデックスのカウンター
    cnt = 0

    for s in S:
        if s == t[cnt]:
            cnt += 1
            if cnt == 3:
                return True
    return False


if __name__ == "__main__":
    main()
