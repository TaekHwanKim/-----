"""
문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
"""
'''
최초 코딩

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while True:
        if scoville[0] < K:
            scoville[0] = scoville[0] + scoville[1]*2
            del scoville[1]
            scoville.sort()
            answer += 1
        else:
            break
    if scoville[-1] < K:
        answer = -1
    return answer

'''
# 최종 코딩
import heapq                 # 시간복잡도를 줄이기 위한 heapq 사용
def solution(scoville, K):
    answer = 0
    item = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1:
            break
        if scoville[0] < K:           # while 문 안에서 min함수 사용시 반복 횟수만큼 작동하기 때문에 자원의 손실이 큼 따라서 heapq의 성질을 이용한 첫번째 인덱스 사용
            item = heapq.heappop(scoville) + heapq.heappop(scoville)*2
            heapq.heappush(scoville, item)
            answer += 1
        else:
            break
    if max(scoville) < K:
        answer = -1
    return answer