CORRELATED_GROUPS = [

    [
        "BTC/USDT",
        "ETH/USDT",
        "SOL/USDT"
    ],

    [
        "BNB/USDT",
        "BTC/USDT"
    ]
]


def is_overexposed(
    symbol,
    open_positions
):
    for group in CORRELATED_GROUPS:

        if symbol not in group:
            continue

        count = 0

        for pos in open_positions:

            if pos in group:
                count += 1

        if count >= 2:
            return True

    return False