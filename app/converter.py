"""単位変換モジュール"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """摂氏から華氏に変換"""
    return celsius * 1.8 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """華氏から摂氏に変換"""
    return (fahrenheit - 32) / 1.8


def km_to_miles(km: float) -> float:
    """キロメートルからマイルに変換"""
    return km * 0.621371


def kg_to_pounds(kg: float) -> float:
    """キログラムからポンドに変換（バグあり: 係数が間違っている）"""
    return kg * 2.0
