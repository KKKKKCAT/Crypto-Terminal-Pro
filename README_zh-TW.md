<p align="center">
<img src="https://raw.githubusercontent.com/KKKKKCAT/Crypto-Terminal-Pro/refs/heads/main/assets/Crypto-Terminal-Pro-logo.webp" alt="Crypto Terminal Pro" width="150">
</p>
<h1 align="center">Crypto Terminal Pro</h1>

> 🚀 終極的加密貨幣市場可視化工具，直接呈現在你的終端機

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square&logo=mit)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square&logo=github)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square&logo=github)](https://github.com/KKKKKCAT/Crypto-Terminal-Pro)
[![Github Stars](https://img.shields.io/github/stars/KKKKKCAT/Crypto-Terminal-Pro?style=flat-square&logo=github)](https://github.com/KKKKKCAT/Crypto-Terminal-Pro/stargazers)


[![Telegram group](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.swo.moe%2Fstats%2Ftelegram%2Fkkcatblog&query=count&color=2CA5E0&label=Telegram%20Group&logo=telegram&cacheSeconds=3600&style=flat-square)](https://t.me/kkcatblog) [![Telegram channel](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.swo.moe%2Fstats%2Ftelegram%2Fkkkkkcat&query=count&color=2CA5E0&label=Telegram%20Channel&logo=telegram&cacheSeconds=3600&style=flat-square)](https://t.me/kkkkkcat) [![X (Twitter)](https://img.shields.io/badge/any_text-Follow-blue?color=2CA5E0&label=Twitter&logo=X&cacheSeconds=3600&style=flat-square)](https://x.com/intent/follow?screen_name=kcat88888)

<p align="center">
  <img src="https://github.com/KKKKKCAT/Crypto-Terminal-Pro/blob/main/assets/screenshot1.gif" alt="Demo 截圖" width="800">
</p>

<p align="center">
  <img src="https://github.com/KKKKKCAT/Crypto-Terminal-Pro/blob/main/assets/screenshot2.webp" alt="Demo 截圖" width="800">
</p>

## ✨ 亮點特色

- 📊 即時加密貨幣市場數據可視化
- 🎯 支援多個交易所（Binance 與 OKX）
- 📈 專業級 K 線圖表
- 📕 實時訂單簿深度顯示
- ⚡ 高效能數據流傳輸
- 🔄 自動刷新與即時更新
- 🌙 基於終端機的使用者介面
- 🎨 依價格變化顯示顏色編碼

## 🚀 快速上手

### 📦 安裝

```bash
wget https://raw.githubusercontent.com/KKKKKCAT/Crypto-Terminal-Pro/refs/heads/main/Crypto-Terminal-Pro.py

# 安裝依賴項
pip install python-binance
pip install python-okx
pip install windows-curses  # 僅限 Windows 系統
```

### 🔧 配置

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

### 💫 啟動應用程式

```bash
python3 Crypto-Terminal-Pro.py
```

## 🎮 操作控制

| 按鍵 | 功能         |
|------|--------------|
| `j`  | 向下滾動     |
| `k`  | 向上滾動     |
| `q`  | 退出應用程式 |

## 📊 支援市場

### 💎 Binance
- `現貨交易`
- `期貨交易`

### 🌟 OKX
- `現貨交易`
- `期貨交易`

## 🛠️ 開發指引

```bash
# Fork 本專案
# Clone 到本地端
git clone https://github.com/YOUR_USERNAME/Crypto-Terminal-Pro.git

# 建立新功能分支
git checkout -b feature/amazing-feature

# 提交更改
git commit -m '✨ 新增驚人的功能'

# 推送分支
git push origin feature/amazing-feature

# 建立 Pull Request
```

## 🤝 貢獻指南

開源社群的魅力在於學習、激勵以及創造，任何貢獻都將受到 **誠摯的感謝**。

參見 [貢獻指南](CONTRIBUTING.md) 獲取更多信息。

## 📝 授權條款

此專案基於 MIT 授權。詳情請參見 [LICENSE](LICENSE) 文件。

## 💫 特別鳴謝

- [python-binance](https://github.com/sammchardy/python-binance)
- [okx-connector](https://github.com/okxapi/python-okx)
- [curses](https://docs.python.org/3/library/curses.html)

## 📬 聯繫方式

👤 **KKKKKCAT**
- Telegram: [@kkkkkcat](https://t.me/kkkkkcat)
- Github: [@KKKKKCAT](https://github.com/KKKKKCAT)

---

<p align="center">由 <a href="https://github.com/KKKKKCAT">KKKKKCAT</a> 用 ❤️ 製作</p>

## Star 歷史記錄
[![Star History Chart](https://api.star-history.com/svg?repos=KKKKKCAT/Crypto-Terminal-Pro&type=Date)](https://star-history.com/#KKKKKCAT/Crypto-Terminal-Pro&Date)

