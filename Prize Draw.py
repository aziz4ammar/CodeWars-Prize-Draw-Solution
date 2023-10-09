def rank(st, we, n):
    if not st:
        return "No participants"

    names = st.split(",")
    
    if n > len(names):
        return "Not enough participants"
    
    weighted_scores = []
    
    for i, name in enumerate(names):
        score = (sum(ord(char.lower()) - ord('a') + 1 for char in name) + len(name)) * we[i]
        weighted_scores.append((name, score))
    
    weighted_scores.sort(key=lambda x: (-x[1], x[0]))
    
    return weighted_scores[n - 1][0]