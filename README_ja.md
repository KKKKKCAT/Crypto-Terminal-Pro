<p align="center">
<img src="https://raw.githubusercontent.com/KKKKKCAT/Crypto-Terminal-Pro/refs/heads/main/assets/Crypto-Terminal-Pro-logo.webp" alt="Crypto Terminal Pro" width="150">
</p>
<h1 align="center">Crypto Terminal Pro</h1>

> 🚀 終極の仮想通貨市場ビジュアライゼーションをあなたのターミナルで

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square&logo=mit)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square&logo=github)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square&logo=github)](https://github.com/KKKKKCAT/Crypto-Terminal-Pro)
[![Github Stars](https://img.shields.io/github/stars/KKKKKCAT/Crypto-Terminal-Pro?style=flat-square&logo=github)](https://github.com/KKKKKCAT/Crypto-Terminal-Pro/stargazers)


[![Telegram group](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.swo.moe%2Fstats%2Ftelegram%2Fkkcatblog&query=count&color=2CA5E0&label=Telegram%20Group&logo=telegram&cacheSeconds=3600&style=flat-square)](https://t.me/kkcatblog) [![Telegram channel](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.swo.moe%2Fstats%2Ftelegram%2Fkkkkkcat&query=count&color=2CA5E0&label=Telegram%20Channel&logo=telegram&cacheSeconds=3600&style=flat-square)](https://t.me/kkkkkcat) [![X (Twitter)](https://img.shields.io/badge/any_text-Follow-blue?color=2CA5E0&label=Twitter&logo=X&cacheSeconds=3600&style=flat-square)](https://x.com/intent/follow?screen_name=kcat88888)

<p align="center">
  <img src="https://github.com/KKKKKCAT/Crypto-Terminal-Pro/blob/main/assets/screenshot1.gif" alt="デモ スクリーンショット" width="800">
</p>

<p align="center">
  <img src="https://github.com/KKKKKCAT/Crypto-Terminal-Pro/blob/main/assets/screenshot2.webp" alt="デモ スクリーンショット" width="800">
</p>

## ✨ 特徴

- 📊 仮想通貨市場のリアルタイムデータビジュアライゼーション
- 🎯 マルチ取引所対応（Binance & OKX）
- 📈 プロフェッショナル品質のローソク足チャート
- 📕 リアルタイムの注文板の深度情報
- ⚡ 高性能データストリーミング
- 🔄 自動更新とリアルタイムアップデート
- 🌙 ターミナルベースのUI
- 🎨 価格変動に基づいたカラフルなコード表示

## 🚀 クイックスタート

### 📦 インストール

```bash
wget https://raw.githubusercontent.com/KKKKKCAT/Crypto-Terminal-Pro/refs/heads/main/Crypto-Terminal-Pro.py

# 依存関係のインストール
pip install python-binance
pip install python-okx
pip install windows-curses  # Windowsのみ
```

### 🔧 設定

```python
tracked_symbols = [
 {"symbol": "BTCUSDT", "decimals": 2, "exchange": "binance", "market": "spot"}, 
 {"symbol": "BTCUSDT", "decimals": 2, "exchange": "binance", "market": "futures"}, 
 {"symbol": "BTC-USDT", "decimals": 2, "exchange": "okx", "market": "spot"},
 {"symbol": "ETHUSDT", "decimals": 2, "exchange": "binance", "market": "spot"}, 
 {"symbol": "XRPUSDT", "decimals": 5, "exchange": "binance", "market": "spot"}, 
 {"symbol": "PEPEUSDT", "decimals": 8, "exchange": "binance", "market": "spot"}, 
 {"symbol": "BNBUSDT", "decimals": 2, "exchange": "binance", "market": "spot"},
 {"symbol": "AI16ZUSDT", "decimals": 5, "exchange": "binance", "market": "futures"}
]
```

### 💫 アプリケーションの起動

```bash
python3 Crypto-Terminal-Pro.py
```

## 🎮 操作方法

| キー | アクション      |
|------|----------------|
| `j`  | 下にスクロール |
| `k`  | 上にスクロール |
| `q`  | 終了           |

## 📊 サポートされているマーケット

### 💎 Binance
- `現物`
- `先物`

### 🌟 OKX
- `現物`
- `先物`

### 🥘 Bitget (v1.0.2 support)
- `現物`
- `先物`

## 🛠️ 開発手順

```bash
# このリポジトリをフォーク
# フォークをクローン
git clone https://github.com/YOUR_USERNAME/Crypto-Terminal-Pro.git

# 機能ブランチを作成
git checkout -b feature/amazing-feature

# 変更をコミット
git commit -m '✨ 素晴らしい機能を追加'

# ブランチをプッシュ
git push origin feature/amazing-feature

# プルリクエストを作成
```

## 🤝 貢献

オープンソースコミュニティは、学び、インスピレーションを受け、新たな創造をする場です。あなたの貢献は **大歓迎** です。

詳細は [貢献ガイドライン](CONTRIBUTING.md) をご覧ください。

## 📝 ライセンス

このプロジェクトは MIT ライセンスの下で提供されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 💫 感謝

- [python-binance](https://github.com/sammchardy/python-binance)
- [okx-connector](https://github.com/okxapi/python-okx)
- [curses](https://docs.python.org/3/library/curses.html)

## 📬 お問い合わせ

👤 **KKKKKCAT**
- Telegram: [@kkkkkcat](https://t.me/kkkkkcat)
- Github: [@KKKKKCAT](https://github.com/KKKKKCAT)

---

<p align="center">❤️ を込めて作成した <a href="https://github.com/KKKKKCAT">KKKKKCAT</a> より</p>

## スター履歴
[![Star History Chart](https://api.star-history.com/svg?repos=KKKKKCAT/Crypto-Terminal-Pro&type=Date)](https://star-history.com/#KKKKKCAT/Crypto-Terminal-Pro&Date)

