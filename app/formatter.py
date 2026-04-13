"""文字列フォーマットモジュール"""

import os, sys, json
import re
from datetime import datetime


def format_date(year: int, month: int, day: int) -> str:
    dt = datetime(year, month, day)
    return dt.strftime("%Y/%m/%d")


def format_currency(amount):
    if amount >= 0:
        return "¥{:,}".format(int(amount))
    else:
        return "-¥{:,}".format(int(abs(amount)))

def truncate_string(text: str, max_length: int) -> str:
    if len(text) <= max_length:
        return text
    else:
        return text[:max_length - 3] + "..."

x = 1
y = 2
z = x+y
