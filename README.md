# JBS CI/CD ハンズオン デモ

GitHub Actions を使った CI/CD パイプラインの体験用リポジトリ。

## セットアップ

```bash
pip install -r requirements.txt
```

## テスト実行

```bash
pytest --cov=app tests/
```

## Lint

```bash
ruff check .
```
