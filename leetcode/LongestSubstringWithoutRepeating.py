
def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0
    for i, char in enumerate(s):
        # 이미 등장했던 문자라면 'start' 위치 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:  # 최대 부분 문자열 길이 갱신
            max_length = max(max_length, i - start + 1)

        # 현재 문자의 위치 삽입
        used[char] = i

    return max_length


print(lengthOfLongestSubstring("abcabcbb"))
