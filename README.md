# Test02 - 計算機能Webアプリケーション

このリポジトリには、基本的なPython計算機能をWebアプリケーションとして提供するFlaskアプリが含まれています。

## 🌐 デプロイ済みアプリ

Railway上でデプロイされており、ブラウザから直接アクセスして計算機能をテストできます。

## 📁 ファイル構成

- `test.py` - FlaskによるWebアプリケーション（メインファイル）
- `requirements.txt` - Python依存関係
- `Procfile` - Railway/Heroku用のプロセス設定
- `README.md` - このファイル

## 🚀 機能

### Webインターフェース
- 美しいレスポンシブデザイン
- リアルタイム計算結果表示
- 日本語対応UI

### API エンドポイント
- `POST /api/add` - 足し算計算
- `POST /api/multiply` - 掛け算計算  
- `POST /api/is_even` - 偶数判定
- `GET /api/run_all_tests` - 全テスト実行

### 計算機能
- ➕ 足し算関数のテスト
- ✖️ 掛け算関数のテスト  
- 🔢 偶数判定関数のテスト
- 🧪 全テスト一括実行

## 💻 ローカル実行方法

```bash
# 依存関係のインストール
pip install -r requirements.txt

# アプリケーション実行
python test.py
```

その後、ブラウザで `http://localhost:5000` にアクセス

## 🛠️ 技術スタック

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Deployment**: Railway
- **Web Server**: Gunicorn

## 👨‍💻 作成者

obinson-consulting-mizutani

