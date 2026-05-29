POSITIONS = {}


def add_position(
    symbol,
    position_data
):
    """
    Добавить позицию
    """

    POSITIONS[symbol] = position_data


def remove_position(
    symbol
):
    """
    Удалить позицию
    """

    if symbol in POSITIONS:
        del POSITIONS[symbol]


def get_position(
    symbol
):
    """
    Получить позицию
    """

    return POSITIONS.get(symbol)


def has_position(
    symbol
):
    """
    Проверить наличие позиции
    """

    return symbol in POSITIONS


def get_all_positions():
    """
    Получить все позиции
    """

    return POSITIONS


def count_positions():
    """
    Количество открытых позиций
    """

    return len(POSITIONS)


def clear_positions():
    """
    Очистить все позиции
    """

    POSITIONS.clear()


def update_position(
    symbol,
    key,
    value
):
    """
    Обновить параметр позиции
    """

    if symbol not in POSITIONS:
        return False

    POSITIONS[symbol][key] = value

    return True


def get_position_side(
    symbol
):
    """
    LONG / SHORT
    """

    position = get_position(symbol)

    if not position:
        return None

    return position.get("side")


def get_position_entry(
    symbol
):
    """
    Цена входа
    """

    position = get_position(symbol)

    if not position:
        return None

    return position.get("entry")


def get_position_size(
    symbol
):
    """
    Размер позиции
    """

    position = get_position(symbol)

    if not position:
        return None

    return position.get("size")