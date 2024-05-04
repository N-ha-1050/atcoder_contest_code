from collections import deque


def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    res = solve(N, A)
    print(res)


def solve(N, A):
    deq = deque()
    cnt = 0
    for a in A:
        while deq:
            b = deq.pop()
            if a != b:
                deq.append(b)
                break
            cnt -= 1
            a += 1
        deq.append(a)
        cnt += 1
    return cnt


if __name__ == "__main__":
    main()
