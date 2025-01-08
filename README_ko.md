<p align="center">
<img src="https://raw.githubusercontent.com/KKKKKCAT/Crypto-Terminal-Pro/refs/heads/main/assets/Crypto-Terminal-Pro-logo.webp" alt="Crypto Terminal Pro" width="150">
</p>
<h1 align="center">Crypto Terminal Pro</h1>

> 🚀 궁극의 암호화폐 시장 시각화, 당신의 터미널에서 제공

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square&logo=mit)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square&logo=github)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square&logo=github)](https://github.com/KKKKKCAT/Crypto-Terminal-Pro)
[![Github Stars](https://img.shields.io/github/stars/KKKKKCAT/Crypto-Terminal-Pro?style=flat-square&logo=github)](https://github.com/KKKKKCAT/Crypto-Terminal-Pro/stargazers)


[![Telegram group](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.swo.moe%2Fstats%2Ftelegram%2Fkkcatblog&query=count&color=2CA5E0&label=Telegram%20Group&logo=telegram&cacheSeconds=3600&style=flat-square)](https://t.me/kkcatblog) [![Telegram channel](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.swo.moe%2Fstats%2Ftelegram%2Fkkkkkcat&query=count&color=2CA5E0&label=Telegram%20Channel&logo=telegram&cacheSeconds=3600&style=flat-square)](https://t.me/kkkkkcat) [![X (Twitter)](https://img.shields.io/badge/any_text-Follow-blue?color=2CA5E0&label=Twitter&logo=X&cacheSeconds=3600&style=flat-square)](https://x.com/intent/follow?screen_name=kcat88888)

<p align="center">
  <img src="https://github.com/KKKKKCAT/Crypto-Terminal-Pro/blob/main/assets/screenshot1.gif" alt="데모 스크린샷" width="800">
</p>

<p align="center">
  <img src="https://github.com/KKKKKCAT/Crypto-Terminal-Pro/blob/main/assets/screenshot2.webp" alt="데모 스크린샷" width="800">
</p>

## ✨ 주요 기능

- 📊 실시간 암호화폐 시장 데이터 시각화
- 🎯 멀티 거래소 지원 (Binance & OKX)
- 📈 전문 수준의 캔들스틱 차트
- 📕 실시간 주문서 깊이 표시
- ⚡ 고성능 데이터 스트리밍
- 🔄 자동 새로고침 및 실시간 업데이트
- 🌙 터미널 기반 UI
- 🎨 가격 변동에 따른 색상 표시

## 🚀 빠른 시작

### 📦 설치

```bash
wget https://raw.githubusercontent.com/KKKKKCAT/Crypto-Terminal-Pro/refs/heads/main/Crypto-Terminal-Pro.py

# 의존성 설치
pip install python-binance
pip install python-okx
pip install windows-curses  # Windows 전용
```

### 🔧 설정

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

### 💫 애플리케이션 실행

```bash
python3 Crypto-Terminal-Pro.py
```

## 🎮 조작 방법

| 키  | 동작          |
|-----|---------------|
| `j` | 아래로 스크롤 |
| `k` | 위로 스크롤   |
| `q` | 종료          |

## 📊 지원하는 시장

### 💎 Binance
- `현물`
- `선물`

### 🌟 OKX
- `현물`
- `선물`

## 🛠️ 개발 가이드

```bash
# 이 리포지토리를 포크
# 포크한 리포지토리 클론
git clone https://github.com/YOUR_USERNAME/Crypto-Terminal-Pro.git

# 새로운 기능 브랜치 생성
git checkout -b feature/amazing-feature

# 변경 사항 커밋
git commit -m '✨ 놀라운 기능 추가'

# 브랜치 푸시
git push origin feature/amazing-feature

# 풀 리퀘스트 생성
```

## 🤝 기여

오픈소스 커뮤니티는 학습, 영감, 창조의 놀라운 장소입니다. 여러분의 기여는 **대환영**입니다.

자세한 내용은 [기여 가이드라인](CONTRIBUTING.md)을 참조하세요.

## 📝 라이선스

이 프로젝트는 MIT 라이선스에 따라 제공됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 💫 감사의 말

- [python-binance](https://github.com/sammchardy/python-binance)
- [okx-connector](https://github.com/okxapi/python-okx)
- [curses](https://docs.python.org/3/library/curses.html)

## 📬 연락처

👤 **KKKKKCAT**
- Telegram: [@kkkkkcat](https://t.me/kkkkkcat)
- Github: [@KKKKKCAT](https://github.com/KKKKKCAT)

---

<p align="center">❤️로 제작한 <a href="https://github.com/KKKKKCAT">KKKKKCAT</a></p>

## 스타 기록
[![Star History Chart](https://api.star-history.com/svg?repos=KKKKKCAT/Crypto-Terminal-Pro&type=Date)](https://star-history.com/#KKKKKCAT/Crypto-Terminal-Pro&Date)


