def main():
    S = input()
    res = solve(S)
    print(res)


def solve(S: str) -> int:
    cnt = 0
    N = len(S)
    for i in range(N):
        if S[i] != "A":
            continue
        for j in range(i + 1, N):
            if S[j] != "B":
                continue
            k = j + (j - i)
            if k >= N:
                break
            if S[k] == "C":
                cnt += 1
    return cnt


if __name__ == "__main__":
    main()
