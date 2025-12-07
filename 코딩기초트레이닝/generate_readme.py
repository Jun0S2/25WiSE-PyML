items = [
    {
        "title": "n의 배수",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181937",
        "note": "python의 삼항연산 계산법",
        "path": "./코딩기초트레이닝/n의배수.py"
    },
    {
        "title": "대문자로 바꾸기",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181877",
        "note": "upper()",
        "path": "./코딩기초트레이닝/대문자로바꾸기.py"
    },
    {
        "title": "두 수의 연산값 비교하기",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181938",
        "note": "str(), int()",
        "path": "./코딩기초트레이닝/두수의연산값비교하기.py"
    },
    {
        "title": "문자열곱하기",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181940",
        "note": "for x in range(x)",
        "path": "./코딩기초트레이닝/문자열곱하기.py"
    },
    {
        "title": "마지막 두 원소",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181927",
        "note": "last element: num_list[-1], .append()",
        "path": "./코딩기초트레이닝/마지막두원소.py"
    },
    {
        "title": "이어붙인 수",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181928",
        "note": '"".join( ) 사용',
        "path": "./코딩기초트레이닝/이어붙인수.py"
    },
]

with open("README.md", "w", encoding="utf-8") as f:
    f.write("# 파이썬 기초 문법 문제 정리\n\n")
    f.write("| 문제 | 프로그래머스 링크 | 비고 | 코드 링크 |\n")
    f.write("|---|---|---|---|\n")
    for it in items:
        f.write(
            f"| {it['title']} | [링크]({it['link']}) | {it['note']} | [링크]({it['path']}) |\n"
        )
