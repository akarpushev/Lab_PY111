from typing import List


def reverse_string(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
        return s

def reverse_string_edit(s: List[str]) -> None:
    idx = len(s) // 2
    s[:idx], s[-1:-idx - 1:-1] = s[-1:-idx -1:-1], s[:idx]
    return s

print(reverse_string([1, 2, 3]))

print(reverse_string_edit([1, 2, 3]))


