<p align="center">
<img src="https://raw.githubusercontent.com/KKKKKCAT/Crypto-Terminal-Pro/refs/heads/main/assets/Crypto-Terminal-Pro-logo.webp" alt="Crypto Terminal Pro" width="150">
</p>
<h1 align="center">Crypto Terminal Pro</h1>

> 🚀 Ultimate crypto market visualization in your terminal

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square&logo=mit)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square&logo=github)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square&logo=github)](https://github.com/KKKKKCAT/Crypto-Terminal-Pro)
[![Github Stars](https://img.shields.io/github/stars/KKKKKCAT/Crypto-Terminal-Pro?style=flat-square&logo=github)](https://github.com/KKKKKCAT/Crypto-Terminal-Pro/stargazers)


[![Telegram group](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.swo.moe%2Fstats%2Ftelegram%2Fkkcatblog&query=count&color=2CA5E0&label=Telegram%20Group&logo=telegram&cacheSeconds=3600&style=flat-square)](https://t.me/kkcatblog) [![Telegram channel](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.swo.moe%2Fstats%2Ftelegram%2Fkkkkkcat&query=count&color=2CA5E0&label=Telegram%20Channel&logo=telegram&cacheSeconds=3600&style=flat-square)](https://t.me/kkkkkcat) [![X (Twitter)](https://img.shields.io/badge/any_text-Follow-blue?color=2CA5E0&label=Twitter&logo=X&cacheSeconds=3600&style=flat-square)](https://x.com/intent/follow?screen_name=kcat88888)

<p align="center">
  <img src="https://github.com/KKKKKCAT/Crypto-Terminal-Pro/blob/main/assets/screenshot1.gif" alt="Demo Screenshot" width="800">
</p>

<p align="center">
  <img src="https://github.com/KKKKKCAT/Crypto-Terminal-Pro/blob/main/assets/screenshot2.webp" alt="Demo Screenshot" width="800">
</p>

## README

- [English](README.md) - [繁體中文](README_zh-TW.md) - [简体中文](README_zh-CN.md) - [日本語](README_ja.md) - [한국어](README_ko.md) - [Bahasa Indonesia](README_id.md) - [Français](README_fr.md)


## ✨ Highlights

- 📊 Real-time crypto market data visualization
- 🎯 Multi-exchange support (Binance & OKX)
- 📈 Professional-grade candlestick charts
- 📕 Live order book depth
- ⚡ High-performance data streaming
- 🔄 Auto-refresh & real-time updates
- 🌙 Terminal-based UI
- 🎨 Color-coded price movements

## 🚀 Quick Start

### 📦 Installation

```bash
wget https://raw.githubusercontent.com/KKKKKCAT/Crypto-Terminal-Pro/refs/heads/main/Crypto-Terminal-Pro.py

# Install dependencies
pip install python-binance
pip install python-okx
pip install windows-curses  # Windows only
```

### 🔧 Configuration

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

### 💫 Run Application

```bash
python3 Crypto-Terminal-Pro.py
```

## 🎮 Controls

| Key | Action |
|-----|--------|
| `j` | Scroll down |
| `k` | Scroll up |
| `q` | Exit |

## 📊 Supported Markets

### 💎 Binance
- `Spot`
- `Futures`

### 🌟 OKX
- `Spot`
- `Futures`

### 🥘 Bitget (v1.0.2 support)
- `Spot`
- `Futures`

## 🛠️ Development

```bash
# Fork this repository
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Crypto-Terminal-Pro.git

# Create feature branch
git checkout -b feature/amazing-feature

# Commit changes
git commit -m '✨ Add amazing feature'

# Push branch
git push origin feature/amazing-feature

# Create Pull Request
```

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

See [Contributing Guidelines](CONTRIBUTING.md) for more information.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 💫 Acknowledgments

- [python-binance](https://github.com/sammchardy/python-binance)
- [okx-connector](https://github.com/okxapi/python-okx)
- [curses](https://docs.python.org/3/library/curses.html)

## 📬 Contact

👤 **KKKKKCAT**
- Telegram: [@kkkkkcat](https://t.me/kkkkkcat)
- Github: [@KKKKKCAT](https://github.com/KKKKKCAT)

---

<p align="center">Made with ❤️ by <a href="https://github.com/KKKKKCAT">KKKKKCAT</a></p>

## Star History
[![Star History Chart](https://api.star-history.com/svg?repos=KKKKKCAT/Crypto-Terminal-Pro&type=Date)](https://star-history.com/#KKKKKCAT/Crypto-Terminal-Pro&Date)
