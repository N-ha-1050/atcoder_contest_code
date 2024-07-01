def main():
    N, M = map(int, input().split())
    H = [int(h) for h in input().split()]
    res = solve(N, M, H)
    print(res)


def solve(N, M, H):

    # 順番にシミュレーションする
    for i, h in enumerate(H):
        M -= h

        # Mが負になったら(→消毒液を使い切ったら)そこでその一つ前まで
        if M < 0:
            return i

    # 全員できたらNを返す
    return N


if __name__ == "__main__":
    main()
