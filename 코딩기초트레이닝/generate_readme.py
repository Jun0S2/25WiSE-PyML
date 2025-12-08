items = [
    {
        "title": "n의 배수",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181937",
        "note": "python의 삼항연산 계산법",
        "path": "./n의배수.py"
    },
    {
        "title": "대문자로 바꾸기",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181877",
        "note": "upper()",
        "path": "./대문자로바꾸기.py"
    },
    {
        "title": "두 수의 연산값 비교하기",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181938",
        "note": "str(), int()",
        "path": "./두수의연산값비교하기.py"
    },
    {
        "title": "문자열곱하기",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181940",
        "note": "for x in range(x)",
        "path": "./문자열곱하기.py"
    },
    {
        "title": "마지막 두 원소",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181927",
        "note": "last element: num_list[-1], .append()",
        "path": "./마지막두원소.py"
    },
    {
        "title": "이어붙인 수",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181928",
        "note": '"".join( ) 사용',
        "path": "./이어붙인수.py"
    },
    {
        "title": "카운트 업",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181920",
        "note": "list comprehension",
        "path": "./카운트업.py"
    },
    {
        "title": "flag에 따라 다른 값 반환하기",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181933",
        "note": "if-else 문",
        "path": "./flag에따라다른값반환하기.py"
    },
    {
        "title": "n번쨰 원소까지",
        "link" : "https://school.programmers.co.kr/learn/courses/30/lessons/181889",
        "note": "list slicing",
        "path": "./n번째원소까지.py"
    },
    {
        "title": "문자역 붙여서 출력하기",
        "link" : "https://school.programmers.co.kr/learn/courses/30/lessons/181946",
        "note": "fstring, join()",
        "path": "./문자역붙여서출력하기.py"
    },
    {
        "title": "홀짝에따라다른값반환하기",
        "link" : "https://school.programmers.co.kr/learn/courses/30/lessons/181935",
        "note": "삼항 연산 심화, sum(), if-else",
        "path": "./홀짝에따라다른값반환.py"
    },
    {
        "title": "문자열 앞의 n 글자",
        "link" :"https://school.programmers.co.kr/learn/courses/30/lessons/181907",
        "note": "list slice",
        "path": "./문자열앞의n글자.py"
    },
    {
        "title" : "문자열 뒤의 n 글자",
        "link" : "https://school.programmers.co.kr/learn/courses/30/lessons/181910",
        "note": "len(str)",
        "path": "./문자열뒤의n글자.py"
    }, 
    {
        "title" : "첫번째로 나오는 음수",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181896",
        "note": "enumerate()",
        "path": "./첫번째로나오는음수.py"
    },
    {
        "title": "더 크게 합치기",
        "link" : "https://school.programmers.co.kr/learn/courses/30/lessons/181939",
        "note": "str()",
        "path": "./더크게합치기.py"
    },
    {
        "title": "문자 리스트를 문자열로 변환하기",
        "link": "https://school.programmers.co.kr/learn/courses/30/lessons/181911",
        "note": "join(),for lop",
        "path": "./문자리스트를문자열로변환하기.py"
    }
]

with open("README.md", "w", encoding="utf-8") as f:
    f.write("# 파이썬 기초 문법 문제 정리\n\n")
    f.write("| 문제 | 프로그래머스 링크 | 비고 | 코드 링크 |\n")
    f.write("|---|---|---|---|\n")
    for it in items:
        f.write(
            f"| {it['title']} | [링크]({it['link']}) | {it['note']} | [링크]({it['path']}) |\n"
        )
