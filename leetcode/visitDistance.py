def solution(dirs):
    visited = {}
    curr = [0, 0]  # (U+/D-, R+/L-)
    for dir in dirs:
        if dir == 'U':
            if curr[0] < 5:
                past = str(curr)
                curr[0] += 1
                visited[past+str(curr)] = 0
                visited[str(curr)+past] = 0
        if dir == 'D':
            if curr[0] > -5:
                past = str(curr)
                curr[0] -= 1
                visited[past+str(curr)] = 0
                visited[str(curr)+past] = 0
        if dir == 'R':
            if curr[1] < 5:
                past = str(curr)
                curr[1] += 1
                visited[past+str(curr)] = 0
                visited[str(curr)+past] = 0
        if dir == 'L':
            if curr[1] > -5:
                past = str(curr)
                curr[1] -= 1
                visited[past+str(curr)] = 0
                visited[str(curr)+past] = 0
    return len(visited)//2
