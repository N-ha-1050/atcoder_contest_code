from collections import deque


def main():
    S = input()
    res = solve(S)
    print("Yes" if res else "No")


def solve(S: str) -> bool:
    que: deque[str] = deque()
    start_chars_idx = {"(": 0, "[": 1, "<": 2}
    end_chars_idx = {")": 0, "]": 1, ">": 2}
    for s in S:
        if s in start_chars_idx:
            que.append(s)
        elif s in end_chars_idx:
            if not que:
                return False
            start_char = que.pop()
            if start_chars_idx[start_char] != end_chars_idx[s]:
                return False
    return not que


if __name__ == "__main__":
    main()
