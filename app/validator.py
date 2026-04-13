"""入力バリデーションモジュール"""

import re


def validate_email(email: str) -> bool:
    """メールアドレスの形式チェック"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))


def validate_age(age: int) -> bool:
    """年齢の範囲チェック（0〜150）"""
    return 0 <= age <= 150


def validate_username(username: str) -> bool:
    """ユーザー名の形式チェック（3〜20文字、英数字とアンダースコアのみ）"""
    if len(username) < 3 or len(username) > 20:
        return False
    return bool(re.match(r"^[a-zA-Z0-9_]+$", username))


def sanitize_input(text: str) -> str:
    """HTMLタグを除去する"""
    return re.sub(r"<[^>]+>", "", text)
