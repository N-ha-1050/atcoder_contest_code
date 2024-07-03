def main():
    S, T = input().split()
    res = solve(S, T)
    print("Yes" if res else "No")


def solve(S, T):
    N = len(S)
    for w in range(1, N):
        for c in range(w):
            t = ""
            for i in range(c, N, w):
                # range(c, N, w) は、cから始めてN未満の範囲でwずつ増やしていくことができる
                t += S[i]
            # 一致するものが一つでも見つかればその時点でYes
            if t == T:
                return True
    return False


if __name__ == "__main__":
    main()
