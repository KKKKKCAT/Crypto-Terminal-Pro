<p align="center">
<img src="https://raw.githubusercontent.com/KKKKKCAT/Crypto-Terminal-Pro/refs/heads/main/assets/Crypto-Terminal-Pro-logo.webp" alt="Crypto Terminal Pro" width="150">
</p>
<h1 align="center">Crypto Terminal Pro</h1>

> 🚀 终极的加密货币市场可视化工具，直接呈现在你的终端机

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square&logo=mit)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square&logo=github)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square&logo=github)](https://github.com/KKKKKCAT/Crypto-Terminal-Pro)
[![Github Stars](https://img.shields.io/github/stars/KKKKKCAT/Crypto-Terminal-Pro?style=flat-square&logo=github)](https://github.com/KKKKKCAT/Crypto-Terminal-Pro/stargazers)


[![Telegram group](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.swo.moe%2Fstats%2Ftelegram%2Fkkcatblog&query=count&color=2CA5E0&label=Telegram%20Group&logo=telegram&cacheSeconds=3600&style=flat-square)](https://t.me/kkcatblog) [![Telegram channel](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.swo.moe%2Fstats%2Ftelegram%2Fkkkkkcat&query=count&color=2CA5E0&label=Telegram%20Channel&logo=telegram&cacheSeconds=3600&style=flat-square)](https://t.me/kkkkkcat) [![X (Twitter)](https://img.shields.io/badge/any_text-Follow-blue?color=2CA5E0&label=Twitter&logo=X&cacheSeconds=3600&style=flat-square)](https://x.com/intent/follow?screen_name=kcat88888)

<p align="center">
  <img src="https://github.com/KKKKKCAT/Crypto-Terminal-Pro/blob/main/assets/screenshot1.gif" alt="Demo 截图" width="800">
</p>

<p align="center">
  <img src="https://github.com/KKKKKCAT/Crypto-Terminal-Pro/blob/main/assets/screenshot2.webp" alt="Demo 截图" width="800">
</p>

## ✨ 亮点特色

- 📊 即时加密货币市场数据可视化
- 🎯 支援多个交易所（Binance 与 OKX）
- 📈 专业级 K 线图表
- 📕 实时订单簿深度显示
- ⚡ 高效能数据流传输
- 🔄 自动刷新与即时更新
- 🌙 基于终端机的使用者介面
- 🎨 依价格变化显示颜色编码

## 🚀 快速上手

### 📦 安装

```bash
wget https://raw.githubusercontent.com/KKKKKCAT/Crypto-Terminal-Pro/refs/heads/main/Crypto-Terminal-Pro.py

# 安装依赖项
pip install python-binance
pip install python-okx
pip install windows-curses  # 仅限 Windows 系统
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

### 💫 启动应用程式

```bash
python3 Crypto-Terminal-Pro.py
```

## 🎮 操作控制

| 按键 | 功能         |
|------|--------------|
| `j`  | 向下滚动     |
| `k`  | 向上滚动     |
| `q`  | 退出应用程式 |

## 📊 支援市场

### 💎 Binance
- `现货交易`
- `期货交易`

### 🌟 OKX
- `现货交易`
- `期货交易`

## 🛠️ 开发指引

```bash
# Fork 本专案
# Clone 到本地端
git clone https://github.com/YOUR_USERNAME/Crypto-Terminal-Pro.git

# 建立新功能分支
git checkout -b feature/amazing-feature

# 提交更改
git commit -m '✨ 新增惊人的功能'

# 推送分支
git push origin feature/amazing-feature

# 建立 Pull Request
```

## 🤝 贡献指南

开源社群的魅力在于学习、激励以及创造，任何贡献都将受到 **诚挚的感谢**。

参见 [贡献指南](CONTRIBUTING.md) 获取更多信息。

## 📝 授权条款

此专案基于 MIT 授权。详情请参见 [LICENSE](LICENSE) 文件。

## 💫 特别鸣谢

- [python-binance](https://github.com/sammchardy/python-binance)
- [okx-connector](https://github.com/okxapi/python-okx)
- [curses](https://docs.python.org/3/library/curses.html)

## 📬 联繫方式

👤 **KKKKKCAT**
- Telegram: [@kkkkkcat](https://t.me/kkkkkcat)
- Github: [@KKKKKCAT](https://github.com/KKKKKCAT)

---

<p align="center">由 <a href="https://github.com/KKKKKCAT">KKKKKCAT</a> 用 ❤️ 製作</p>

## Star 历史记录
[![Star History Chart](https://api.star-history.com/svg?repos=KKKKKCAT/Crypto-Terminal-Pro&type=Date)](https://star-history.com/#KKKKKCAT/Crypto-Terminal-Pro&Date)
