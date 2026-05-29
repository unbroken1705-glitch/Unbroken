from ai.score_engine import (
    get_confidence
)


def evaluate_signal(
    trend_ok,
    volume_ok,
    volatility_ok,
    btc_ok,
    structure_ok
):
    confidence = get_confidence(
        trend_ok,
        volume_ok,
        volatility_ok,
        btc_ok,
        structure_ok
    )

    return {
        "confidence": confidence,
        "approved": confidence >= 70
    }