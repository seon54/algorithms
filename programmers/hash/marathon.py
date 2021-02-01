def solution(participant, completion):
    d = {}
    for p in participant:
        if p not in d:
            d[p] = 1
        else:
            d[p] = d.get(p) + 1
            
    for c in completion:
        d[c] = d.get(c) - 1
        
    for k, v in d.items():
        if v == 1:
            return k