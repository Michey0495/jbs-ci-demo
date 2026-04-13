from app.formatter import format_date, format_currency, truncate_string


def test_format_date():
    assert format_date(2026, 5, 12) == "2026/05/12"
    assert format_date(2026, 1, 1) == "2026/01/01"


def test_format_currency():
    assert format_currency(1000) == "¥1,000"
    assert format_currency(0) == "¥0"
    assert format_currency(-500) == "-¥500"


def test_truncate_string():
    assert truncate_string("hello", 10) == "hello"
    assert truncate_string("hello world", 8) == "hello..."
