def main():
    S = input()
    res = solve(S)
    print(res)


def solve(S):

    # 大文字と小文字の文字数をそれぞれ数える
    cnt_lower, cnt_upper = 0, 0

    # 各文字について数え上げる
    for s in S:
        if s.islower():
            cnt_lower += 1
        else:
            cnt_upper += 1

    # 数え上げた結果で返り値を条件分岐
    if cnt_lower < cnt_upper:
        return S.upper()
    else:
        return S.lower()


if __name__ == "__main__":
    main()
