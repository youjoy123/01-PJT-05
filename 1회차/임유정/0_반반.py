import sys

sys.stdin = open("_반반.txt")

# 길이 4의 알파벳 대문자로 이루어진 문자열 S가 주어졌을 때, S에 정확히 두 개의 서로 다른 문자가 등장하고, 
# 각 문자가 정확히 두 번 등장하는 지 판별하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.
#     ∙ 첫 번째 줄에 문자열 S가 주어진다.

# [출력]
# 각 테스트 케이스마다
#     ∙ 조건이 만족되면 “Yes”, 아니면 “No” 를 출력하라

S = int(input())
dic = {}
for i in range(S):
    line = list(input())
    dic = sorted(line)
    if dic[0]==dic[1] and dic[2]==dic[3] and dic[1]!=dic[2]:
        print(f'#{i+1} Yes')
    else:
        print(f'#{i+1} No')