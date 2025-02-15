def main():
    S = input().split()
    res = solve(S)
    print(res)


def solve(S: list[str]) -> int:
    N = 4
    M = 2
    people = [(0, 1), (0, 2)]
    all = (1 << N) - 1
    mem = [sum(1 << n for n in person) for person in people]
    for i in range(M):
        if S[i] == "fine":
            mem[i] ^= all
    res = all
    for m in mem:
        res &= m
    for i in range(N):
        if res >> i & 1:
            return i + 1
    return -1


if __name__ == "__main__":
    main()
