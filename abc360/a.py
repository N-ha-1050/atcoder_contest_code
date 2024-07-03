def main():
    S = input()
    res = solve(S)
    print("Yes" if res else "No")


def solve(S):
    # python の index は便利だが、計算量が文字列の長さに比例するため、文字列が長い場合や繰り返される場合(ループの中に含まれる場合)は避ける
    return S.index("R") < S.index("M")


if __name__ == "__main__":
    main()
