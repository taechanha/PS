# - 돌상 N개가 일렬로 놓여있음. 
# - 각 돌상은 왼쪽 혹은 오른쪽 방향을 바라보고 있음
# - 연속한 몇 개의 돌상에 금칠을 할 수 있음
# - 깨달음의 양: |왼쪽 방향 돌상 개수 - 오른쪽 방향 돌상 개수|
# - 얻을 수 있는 최대 깨달음의 양은?

# 0 1 0 0 0 1 0 1 -> 
# 

def solution(arr):
    
    
    
    if all(x < 0 for x in arr):
        return max(arr)

    total = 0
    max_total = 0
    for i, x in enumerate(arr):
        total += x
        if total < 0:  # 다음 수를 더했을 때 음수가 된다면, 다음 수를 더하는 것이 의미가 없어짐
            total = 0            # 추가로, 연속된 수를 선택하는 것이기 때문에, 여태까지 선택한 연속성은 끊겨야함

        max_total = max(max_total, total)
        # 다음 수를 더했을 때 음수가 되는 것이 아니라면 더하고 넘어감
        # 음수가 된다면 건너뛰고 새로 시작

    return max_total

