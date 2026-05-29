import sqlite3
import os

os.makedirs(
    "data",
    exist_ok=True
)

DB_PATH = "data/trades.db"

conn = sqlite3.connect(
    DB_PATH,
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS trades (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    symbol TEXT,
    side TEXT,

    entry REAL,
    exit REAL,

    pnl REAL,

    status TEXT,

    opened_at TEXT,
    closed_at TEXT
)
""")

conn.commit()


def save_trade(
    symbol,
    side,
    entry,
    exit_price,
    pnl,
    status,
    opened_at,
    closed_at
):

    cursor.execute(
        """
        INSERT INTO trades (
            symbol,
            side,
            entry,
            exit,
            pnl,
            status,
            opened_at,
            closed_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            symbol,
            side,
            entry,
            exit_price,
            pnl,
            status,
            opened_at,
            closed_at
        )
    )

    conn.commit()


def get_all_trades():

    cursor.execute(
        """
        SELECT * FROM trades
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()


def get_trade_count():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM trades
        """
    )

    return cursor.fetchone()[0]


def get_total_pnl():

    cursor.execute(
        """
        SELECT SUM(pnl)
        FROM trades
        WHERE status='CLOSED'
        """
    )

    result = cursor.fetchone()[0]

    return result if result else 0


def get_winning_trades():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM trades
        WHERE pnl > 0
        """
    )

    return cursor.fetchone()[0]


def get_losing_trades():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM trades
        WHERE pnl < 0
        """
    )

    return cursor.fetchone()[0]


def get_winrate():

    wins = get_winning_trades()

    losses = get_losing_trades()

    total = wins + losses

    if total == 0:
        return 0

    return round(
        (wins / total) * 100,
        2
    )