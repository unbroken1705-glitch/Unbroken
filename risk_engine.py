from config.settings import (
    MAX_RISK_PER_TRADE,
    MAX_SIMULTANEOUS_POSITIONS,
    DEFAULT_LEVERAGE
)

from core.position_manager import POSITIONS


def can_open_new_position():

    return len(POSITIONS) < MAX_SIMULTANEOUS_POSITIONS


def calculate_position_size(
    balance,
    entry_price,
    stop_price,
    risk_percent=MAX_RISK_PER_TRADE
):
    risk_amount = balance * risk_percent

    stop_distance = abs(
        entry_price - stop_price
    )

    if stop_distance <= 0:
        return 0

    position_size = (
        risk_amount /
        stop_distance
    )

    return round(
        position_size,
        3
    )


def calculate_risk_reward(
    entry,
    stop,
    target
):
    risk = abs(entry - stop)

    reward = abs(target - entry)

    if risk == 0:
        return 0

    return round(
        reward / risk,
        2
    )


def calculate_position_value(
    size,
    price
):
    return round(
        size * price,
        2
    )


def calculate_margin_required(
    size,
    price,
    leverage=DEFAULT_LEVERAGE
):
    position_value = (
        size * price
    )

    return round(
        position_value / leverage,
        2
    )