from botapp import database as db
from random import choice


def get_token(model) -> str:
    """
    Returns randomly generated string
    :return: str
    """
    token = ''
    symbols = "qwertyuioplkjhgfdsazxcvbnm1234567890"
    for _ in range(15):
        s = choice(symbols)
        if choice('ul') == 'u':
            token += s.upper()
        else:
            token += s
    if db.session.query(model).filter(model.binder == token).first():
        get_token(model)
    return token


def collect_info(data: dict) -> str:
    info = "\n"
    for k in data.keys():
        if item := data.get(k):
            if isinstance(item, dict):
                item = collect_info(item)
            info += f"{k}:\n  {item}\n"
    return info

