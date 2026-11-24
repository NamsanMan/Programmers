def solution(users, emoticons):
    answer = []
    rate_combos = []
    row = [0] * len(emoticons)
    def dfs(idx_emt):
        if idx_emt == len(emoticons):
            rate_combos.append(row[:])
            return
        for r in (10, 20 , 30, 40):
            row[idx_emt] = r
            dfs(idx_emt + 1)
    dfs(0)

    results = []        # [[case1에서 구독 명수, 가격], [case2에서 구독 명수, 가격], ...]
    for case in range(len(rate_combos)):
        plus = 0
        sales = 0
        for ppl in range(len(users)):
            cost = 0
            for e in range(len(emoticons)):
                if rate_combos[case][e] >= users[ppl][0]:          # 기준 이상 할인이면 구매
                    cost += emoticons[e] * (100 - rate_combos[case][e]) // 100
            if cost >= users[ppl][1]:                              # 기준 금액 이상이면 가입
                plus += 1
            else:
                sales += cost
        results.append([plus, sales])

    answer = max(results)
    return answer