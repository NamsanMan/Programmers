def solution(cacheSize, cities):
    answer = 0
    cities_lower = []
    for c in cities:
        cities_lower.append(c.lower())
    
    cached = []
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities_lower:
        if city in cached:
            answer += 1
            cached.remove(city)
            cached.append(city)
        else:
            answer += 5
            if len(cached) == cacheSize:
                cached.pop(0)
            cached.append(city)
        
    print(cached)
    return answer