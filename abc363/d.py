def main():
    N = int(input())
    res = solve(N)
    print(res)


def solve(N):
    # コーナーケースの対処
    if N == 1:
        return 0

    N -= 2

    dig = 1  # 答えの桁数
    M = 9  # 桁数がdigの回文数の個数

    # 桁数を求める
    while not N < M:
        N -= M
        if dig % 2 == 0:
            M *= 10
        dig += 1

    d = (dig + 1) // 2  # 真ん中を含む前半部分の長さ
    S = str(N + 10 ** (d - 1))  # 前半部分を文字列として生成
    res = [None for _ in range(dig)]

    # 答えの回文数を生成
    for i in range(d):
        res[i] = res[dig - i - 1] = S[i]

    return "".join(res)


if __name__ == "__main__":
    main()
