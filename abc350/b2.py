from collections import Counter


def main():
    N, Q = map(int, input().split())
    T = [int(t) - 1 for t in input().split()]
    res = solve(N, Q, T)
    print(res)


def solve(N, Q, T):
    return N - sum(map(lambda x: x % 2, Counter(T).values()))


if __name__ == "__main__":
    main()
