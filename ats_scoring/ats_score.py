def calculate_score(matched, required):

    if len(required) == 0:
        return 0

    score = (len(matched) / len(required)) * 100

    return round(score,2)