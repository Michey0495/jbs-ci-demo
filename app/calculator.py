"""シンプルな計算モジュール（ハンズオン用）"""


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b


def power(base: int, exponent: int) -> int:
    return base ** exponent
