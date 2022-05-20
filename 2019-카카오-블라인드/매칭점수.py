def find_a(body):
    word = '<a'
    cnt = 0
    for i in range(len(body) - 1):
        if word == body[i: i + 2]:
            cnt += 1
    return cnt


class Page:
    def __init__(self, idx, basic_score, external_links, link_score) -> None:
        self.idx = idx
        self.basic_score = basic_score
        self.external_links = external_links
        self.link_score = link_score
        self.matching_score = basic_score + link_score


def get_cnt_word(word, body):
    words_list = []
    words = ""
    for s in body + " ":
        if not s.isalpha():
            words_list.append(words)
            words = ""
        else:
            words += s.lower()
    return words_list.count(word.lower())


def solution(word, pages):
    DEBUG = 0
    # 1. 각 페이지를 그림처럼 하나의 객체로 표현
    #   - 웹 페이지 이름: content="https://"
    page_dict = {}
    for idx, page in enumerate(pages):
        content_start_at = page.find(
            "<meta property=\"og:url\" content=\"https://")
        # content_start_at = page.find("content=\"https://")
        content_end_at = page[content_start_at:].find('>')
        # print(page[content_start_at: content_start_at+content_end_at+1])
        start_at = -1
        end_at = -1
        inner_start_at = page[content_start_at:].find('content')
        for i, c in enumerate(page[content_start_at + inner_start_at: content_start_at + inner_start_at + content_end_at+1]):
            if c == '"':
                if start_at == -1:
                    start_at = i
                    continue
                if end_at == -1:
                    end_at = i
        name = page[content_start_at + inner_start_at + start_at +
                    1: inner_start_at + content_start_at+end_at]  # https://example.io"
        # print(name)
    #   - 기본점수: 검색어 등장 횟수(대소 무시), 단어 단위비교, abc | abab abababa -> X  |  aba@aba aba -> 3.
    #             단어: 알파벳 제외한 다른 문자로 구분
        body_start_at = page.find('<body>')
        body_end_at = page.find('</body>')
        flag = 0
        body = ""
        for i, c in enumerate(page[body_start_at: body_end_at]):
            if c == '<':
                flag = 1
            elif c == '>':
                if flag == 1:
                    flag = 0
            if flag == 0:
                body += c

        # 단어 리스트에서 word 찾기 - 단어 리스트를 생성: 알파벳만으로 이루어진 요소
        basic_score = get_cnt_word(word, body)

        #   - 외부 링크 수: <a href="https://~">
        external_links = []
        a_cnt = find_a(page)
        temp_page = page
        for i in range(a_cnt):
            a_start_at = temp_page.find("<a href=\"https://")
            a_end_at = temp_page[a_start_at:].find('>')
            external_link = temp_page[a_start_at +
                                      9: a_start_at + a_end_at - 1]
            external_links.append(external_link)
            temp_page = temp_page[a_start_at + 1:]

        # for each in page.split():
        #     if each.startswith('href="https://'):
        #         external_link = each[6: each.find('>') - 1]
        #         external_links.append(external_link)
        # ------------------------------------------------------------------- #

        page_dict[name] = Page(idx, basic_score, external_links, link_score=0)

    #   - 링크 점수: a 페이지로 링크가 걸린 b, c 페이지 각각의 기본점수 / 그 페이지 각각의 외부 링크 수
    for i, (name, page) in enumerate(page_dict.items()):
        for external_link in page.external_links:
            if not (external_link in page_dict):
                continue
            page_dict[external_link].link_score += page.basic_score / \
                len(page.external_links)

    #   - 매칭점수: 기본점수 + 링크점수
    for i, (name, page) in enumerate(page_dict.items()):
        page.matching_score = page.basic_score + page.link_score

    page_dict = sorted(page_dict.items(),
                       key=lambda item: (-item[1].matching_score, item[1].idx))

    if DEBUG:
        for page in page_dict:
            print(page[0])
            print("index: ", page[1].idx)
            print("기본점수: ", page[1].basic_score)
            print("외부링크: ", page[1].external_links)
            print("링크점수: ", page[1].link_score)
            print("매칭점수: ", page[1].matching_score)
            print("-----------\n")

    return page_dict[0][1].idx


word = 'blind'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

# word = 'Muzi'
# pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
#  "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

res = solution(word, pages)
print(res)
