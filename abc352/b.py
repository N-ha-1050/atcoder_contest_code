def main():
    S = input()
    T = input()
    res = solve(S, T)
    print(*res)


def solve(S, T):
    N = len(S)
    res = [None for _ in range(N)]

    # S のインデックス管理
    idx = 0

    for i, t in enumerate(T):
        if t == S[idx]:
            res[idx] = i + 1
            idx += 1
            if idx == N:
                break
    return res


if __name__ == "__main__":
    main()
