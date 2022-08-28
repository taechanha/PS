# def braces(values):
#     result = []
#     for value in values:
#         stack = []
#         for char in value:
#             if char == '{' or char == '[' or char == '(':
#                 stack.append(char)
#             elif char == '}' or char == ']' or char == ')':
#                 if len(stack) == 0:
#                     result.append('NO')
#                     break
#                 else:
#                     last = stack.pop()
#                     if (last == '{' and char != '}') or (last == '[' and char != ']') or (last == '(' and char != ')'):
#                         result.append('NO')
#                         break

#         if len(stack) == 0:  # and len(result) == 0:
#             result.append('YES')
#         else:
#             result.append('NO')
#     return result


# print(braces(["{{", "{{()"]))


# def programmerStrings(s):
#     # Write your code here
#     # To print results to the standard output you can use print
#     # Example: print "Hello world!"
#     if s.find('programmer') == -1:
#         return 0
#     else:
#         return len(s) - s.rfind('programmer') - len('programmer')


# print(programmerStrings('programmerxxxprozmerqgram'))


# from itertools import combinations
# print(len(list(combinations([4, 5, 6, 10], 3))))

# def largestArea(samples):
#     n = len(samples)
#     dp = [[0 for _ in range(n)] for _ in range(n)]
#     max_area = 0
#     for i in range(n):
#         for j in range(n):
#             if samples[i][j] == 1:
#                 dp[i][j] = 1
#                 if i > 0 and j > 0:
#                     dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
#                 max_area = max(max_area, dp[i][j])
#     return max_area


# print(largestArea([[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# import math
# from collections import defaultdict


# def connectedSum(n, from_, to):
#     # your code here
#     graph = dict()
#     for i in range(len(from_)):
#         if from_[i] in graph:
#             graph[from_[i]].append(to[i])
#         else:
#             graph[from_[i]] = [to[i]]
#         if to[i] in graph:
#             graph[to[i]].append(from_[i])
#         else:
#             graph[to[i]] = [from_[i]]

#     visited = set()
#     cnt = 0
#     for i in range(1, n+1):
#         before = visited.copy()
#         if i not in visited:
#             cnt += math.ceil(math.sqrt(len(dfs(i,
#                              graph, visited)) - len(before)))
#     return cnt


# def dfs(node, graph, visited):
#     visited.add(node)
#     if node in graph:
#         for i in graph[node]:
#             if i not in visited:
#                 dfs(i, graph, visited)
#     return visited


# print(connectedSum(10, [1, 1, 2, 3, 7], [2, 3, 4, 5, 8]))
# connectedSum(10, [1, 1, 2, 3, 7], [2, 3, 4, 5, 8])


def braces(values):
    answer = []
    for s in values:
        stack = []
        for parenthesis in s:
            stack.append(parenthesis)
            flag = 0
            while len(stack) >= 2 and flag != 1:
                if stack[-1] == ")" and stack[-2] == "("\
                        or stack[-1] == "}" and stack[-2] == "{"\
                        or stack[-1] == "]" and stack[-2] == "[":
                    stack.pop(-1)
                    stack.pop(-1)
                else:
                    flag = 1
        if stack == []:
            answer.append("YES")
        else:
            answer.append("NO")

    return answer


print(braces(['[{}]', '[{]}']))
