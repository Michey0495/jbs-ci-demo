"""テキスト統計モジュール"""


def count_words(text: str) -> int:
    """単語数をカウント"""
    if not text.strip():
        return 0
    return len(text.split())


def count_characters(text: str, include_spaces: bool = True) -> int:
    """文字数をカウント"""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def count_lines(text: str) -> int:
    """行数をカウント"""
    if not text:
        return 0
    return len(text.splitlines())


def count_paragraphs(text: str) -> int:
    """段落数をカウント（空行で区切る）"""
    if not text.strip():
        return 0
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


def most_common_word(text: str) -> str:
    """最も頻出する単語を返す"""
    if not text.strip():
        return ""
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return max(frequency, key=frequency.get)


def average_word_length(text: str) -> float:
    """平均単語長を返す"""
    if not text.strip():
        return 0.0
    words = text.split()
    total = sum(len(w) for w in words)
    return total / len(words)
