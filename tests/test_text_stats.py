from app.text_stats import count_words, count_characters


def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("") == 0


def test_count_characters():
    assert count_characters("hello") == 5
