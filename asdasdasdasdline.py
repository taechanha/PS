def solution(k, dic, chat):
    ans = []
    dic_set = set(dic)
    chat = chat.split()
    
    for word in chat:
        word1 = word
        # 모두 .이라면 -> 길이만 비교
        for x in word:
            if x != '.':
                break
        else:
            l = len(word)
            for dic_word in dic:
                if l > len(dic_word):
                    continue
                if l*k >= len(dic_word):
                    found = 1
                    break
            if found:
                ans.append(len(word) * '#'); continue
            
        # 문자만 골라내서 포함되는 게 하나도 없으면 스킵
        yes = 0
        word_set = []
        for ch in word:
            if ch.isalpha():
                word_set.append(ch)
        for w in word_set:
            if any([True for dic_word in dic if dic_word.find(w) != -1]):
                yes = 1
                break
        if not yes:
            ans.append(word)
            continue

        found = 0
        # word 길이가 dic의 모든 요소보다 크다면 -> 아웃
        for dic_word in dic:
            if len(word) <= len(dic_word):
                break
        else:
            ans.append(word)
            continue
        # dic과 매칭되는 게 있다면 -> 매칭 시도
        if word in dic_set:
            ans.append(len(word) * '#'); continue

        # .이 부분적으로 있는 경우 -> 일치하는 애들 찾아서 걔네 제외하고 .의 개수 * k 와 남은 애들의 길이 비교
        found = 0
        c = word1.count('.')
        for dic_word in dic:
            a = cut(dic_word, word1)
            if c > len(a):
                continue
            if c*k >= len(a):
                found = 1
                break
        if found:
            ans.append(len(word1) * '#')
            continue
            
        ans.append(word1)
    return ' '.join(ans)

def cut(a, b):
    b = b.split('.')
    for each in b:
        a = a.replace(each, '')
    return a

k = 3
dic = ["abcde", "cdefg", "efgij"]
chat = ".. ab. cdefgh .gi. .z."
res = solution(k, dic, chat)
print(res)