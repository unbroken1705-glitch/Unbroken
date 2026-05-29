def calculate_score(
    trend_score,
    volume_score,
    volatility_score,
    btc_score,
    structure_score
):
    score = 0

    score += trend_score
    score += volume_score
    score += volatility_score
    score += btc_score
    score += structure_score

    return min(score, 100)


def get_confidence(
    trend_ok,
    volume_ok,
    volatility_ok,
    btc_ok,
    structure_ok
):
    trend_score = 30 if trend_ok else 0

    volume_score = 20 if volume_ok else 0

    volatility_score = 15 if volatility_ok else 0

    btc_score = 20 if btc_ok else 0

    structure_score = 15 if structure_ok else 0

    return calculate_score(
        trend_score,
        volume_score,
        volatility_score,
        btc_score,
        structure_score
    )