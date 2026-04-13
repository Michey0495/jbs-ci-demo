from app.converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    km_to_miles,
    kg_to_pounds,
)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100


def test_km_to_miles():
    result = km_to_miles(10)
    assert abs(result - 6.21371) < 0.001


def test_kg_to_pounds():
    # 1kg = 2.20462 ポンド
    result = kg_to_pounds(1)
    assert abs(result - 2.20462) < 0.001

    result = kg_to_pounds(10)
    assert abs(result - 22.0462) < 0.001
