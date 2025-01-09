import curses
import time
import gc
from binance.client import Client
import okx.MarketData as MarketData
from datetime import datetime, timedelta
from functools import wraps
import requests

tracked_symbols = [
 {"symbol": "BTCUSDT", "decimals": 2, "exchange": "binance", "market": "spot"}, 
 {"symbol": "BTCUSDT", "decimals": 2, "exchange": "binance", "market": "futures"}, 
 {"symbol": "BTC-USDT", "decimals": 2, "exchange": "okx", "market": "spot"},
 {"symbol": "ETHUSDT", "decimals": 2, "exchange": "binance", "market": "spot"}, 
 {"symbol": "XRPUSDT", "decimals": 5, "exchange": "binance", "market": "spot"}, 
 {"symbol": "PEPEUSDT", "decimals": 8, "exchange": "binance", "market": "spot"}, 
 {"symbol": "BNBUSDT", "decimals": 2, "exchange": "binance", "market": "spot"},
 {"symbol": "BTCUSDT", "decimals": 2, "exchange": "bitget", "market": "futures"},
]

CONFIG = {
  'chart': {
      'width': 20,
      'height': 8,
      'candles': 8,
      'refresh_rate': 0.2
  },
  'layout': {
      'padding': 70,
      'items_per_column': 4
  },
  'colors': {
      'up': curses.COLOR_GREEN,
      'down': curses.COLOR_RED,
      'neutral': curses.COLOR_WHITE
  }
}

def retry_on_error(max_retries=3, delay=1):
  def decorator(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          for attempt in range(max_retries):
              try:
                  return func(*args, **kwargs)
              except Exception as e:
                  if attempt == max_retries - 1:
                      print(f"Failed after {max_retries} attempts: {e}")
                      return None
                  time.sleep(delay)
          return None
      return wrapper
  return decorator

class CandleData:
  def __init__(self, open_price, high_price, low_price, close_price):
      self.open = float(open_price)
      self.high = float(high_price)
      self.low = float(low_price)
      self.close = float(close_price)
      self.is_bullish = self.close >= self.open
      
class BitgetClient:
    def __init__(self):
        self.base_url = "https://api.bitget.com"
        
    def get_ticker(self, symbol, market='spot'):
        if market == 'spot':
            response = requests.get(f"{self.base_url}/api/v2/spot/market/tickers?symbol={symbol}")
        else:
            symbol = f"{symbol}_UMCBL"
            response = requests.get(f"{self.base_url}/api/v2/mix/market/ticker?symbol={symbol}&productType=USDT-FUTURES")
        return response.json()
        
    def get_order_book(self, symbol, market='spot'):
        if market == 'spot':
            response = requests.get(f"{self.base_url}/api/v2/spot/market/orderbook?symbol={symbol}&type=step0")
        else:
            response = requests.get(f"{self.base_url}/api/v2/mix/market/merge-depth?symbol={symbol}&productType=USDT-FUTURES")
        return response.json()
        
    def get_klines(self, symbol, interval='1min', limit=30, market='spot'):
        end_time = int(time.time() * 1000)
        if market == 'spot':
            response = requests.get(f"{self.base_url}/api/v2/spot/market/candles?symbol={symbol}&granularity={interval}&limit={limit}&endTime={end_time}")
        else:
            response = requests.get(f"{self.base_url}/api/v2/mix/market/candles?symbol={symbol}&granularity=1m&limit={limit}&endTime={end_time}&productType=USDT-FUTURES&kLineType=MARKET")
        return response.json()

    


@retry_on_error()
def get_candle_data(client, symbol, market, interval='1m', limit=30):
    try:
        if isinstance(client, MarketData.MarketAPI):
            bars = client.get_candlesticks(
                instId=symbol,
                bar=interval,
                limit=str(limit)
            )
            if bars and 'data' in bars:
                candles = []
                for bar in bars['data']:
                    candles.append(CandleData(bar[1], bar[2], bar[3], bar[4]))
                ticker = client.get_ticker(instId=symbol)
                if ticker and 'data' in ticker:
                    current_price = float(ticker['data'][0]['last'])
                    if candles:
                        last_candle = candles[-1]
                        current_candle = CandleData(
                            last_candle.close,
                            max(last_candle.close, current_price),
                            min(last_candle.close, current_price),
                            current_price
                        )
                        candles.append(current_candle)
                return candles
        elif isinstance(client, BitgetClient):
           interval_map = {'1m': '1min', '5m': '5min', '15m': '15min'}
           bitget_interval = interval_map.get(interval, '1min')
           
           klines = client.get_klines(symbol, interval=bitget_interval, limit=limit-1, market=market)
           
           if klines and 'data' in klines and klines['data']:
               candles = []
               for k in klines['data']:
                   open_price = k[1]  
                   high_price = k[2]
                   low_price = k[3] 
                   close_price = k[4]
                   candle = CandleData(open_price, high_price, low_price, close_price)
                   candles.append(candle)
               
               ticker = client.get_ticker(symbol, market=market)
               return candles
           return []
        else:
            if market == "futures":
                klines = client.futures_klines(symbol=symbol, interval=interval, limit=limit)
                ticker = client.futures_symbol_ticker(symbol=symbol)
            else:
                klines = client.get_klines(symbol=symbol, interval=interval, limit=limit-1)
                ticker = client.get_symbol_ticker(symbol=symbol)
                
            current_price = float(ticker['price'])
            candles = [CandleData(k[1], k[2], k[3], k[4]) for k in klines]
            
            if candles:
                last_candle = candles[-1]
                current_candle = CandleData(
                    last_candle.close,
                    max(last_candle.close, current_price),
                    min(last_candle.close, current_price),
                    current_price
                )
                candles.append(current_candle)
            return candles
    except Exception as e:
        print(f"Candle error for {symbol}: {e}")
        return []
  
  

def draw_candlestick(candle, height, min_price, max_price, width=3):
  if max_price == min_price:
      return [" " * width for _ in range(height)]
  
  price_range = max_price - min_price
  high_y = int((max_price - candle.high) * (height - 1) / price_range)
  low_y = int((max_price - candle.low) * (height - 1) / price_range)
  open_y = int((max_price - candle.open) * (height - 1) / price_range)
  close_y = int((max_price - candle.close) * (height - 1) / price_range)
  
  high_y = min(max(high_y, 0), height - 1)
  low_y = min(max(low_y, 0), height - 1)
  open_y = min(max(open_y, 0), height - 1)
  close_y = min(max(close_y, 0), height - 1)
  
  canvas = [[" " for _ in range(width)] for _ in range(height)]
  
  for y in range(min(high_y, low_y), max(high_y, low_y) + 1):
      canvas[y][width // 2] = "│"
  
  body_start = min(open_y, close_y)
  body_end = max(open_y, close_y)
  char = "█" if candle.is_bullish else "▓"
  
  for y in range(body_start, body_end + 1):
      for x in range(width):
          canvas[y][x] = char
  
  return [''.join(line) for line in canvas]

@retry_on_error()
def get_order_book(client, symbol, market, limit=10):
    try:
        if isinstance(client, MarketData.MarketAPI):
            book = client.get_orderbook(
                instId=symbol,
                sz=str(limit)
            )
            if book and 'data' in book and len(book['data']) > 0:
                bids = book['data'][0]['bids'][:10]
                asks = book['data'][0]['asks'][:10]
                return bids, asks
        elif isinstance(client, BitgetClient):
            book = client.get_order_book(symbol, market=market)
            if book and 'data' in book and book['data'] is not None:
                if market == 'spot':
                    bids = book['data']['bids'][:10]
                    asks = book['data']['asks'][:10]
                else:
                    bids = [[str(bid[0]), str(bid[1])] for bid in book['data'].get('bids', [])][:10]
                    asks = [[str(ask[0]), str(ask[1])] for ask in book['data'].get('asks', [])][:10]
                return bids, asks
            return [], []
        else:
            if market == "futures":
                futures_limit = 10
                order_book = client.futures_order_book(symbol=symbol, limit=futures_limit)
            else:
                order_book = client.get_order_book(symbol=symbol, limit=limit)
            bids = order_book["bids"][:10]
            asks = order_book["asks"][:10]
            return bids, asks
        return [], []
    except Exception as e:
        print(f"Order book error for {symbol} ({market}): {e}")
        return [], []

def draw_chart_section(pad, start_row, start_col, candles, symbol, decimals, exchange, market, chart_height=10):
    title = f"{exchange} {symbol} {market}"
    pad.addstr(start_row, start_col, title, curses.color_pair(3))
    
    if not candles:
        return
        
    current_price = candles[-1].close
    price_color = curses.color_pair(1) if candles[-1].is_bullish else curses.color_pair(2)
    
    price_label = "Price: "
    price_value = f"{current_price:,.{decimals}f}"
    
    pad.addstr(start_row + 1, start_col, price_label, curses.color_pair(3))
    pad.addstr(start_row + 1, start_col + len(price_label), price_value, price_color | curses.A_BOLD)
    
    max_price = max(c.high for c in candles)
    min_price = min(c.low for c in candles)
    
    for i in range(chart_height):
        row = start_row + 2 + i
        price = max_price - (i * (max_price - min_price) / (chart_height - 1))
        price_str = f"{price:,.{decimals}f}"
        pad.addstr(row, start_col, " " * 15, curses.color_pair(3))
        pad.addstr(row, start_col, price_str, curses.color_pair(3))
        pad.addstr(row, start_col + len(price_str), "│", curses.color_pair(3))
        
        for j, candle in enumerate(candles):
            candle_x = start_col + len(price_str) + 1 + (j * 2)
            candle_lines = draw_candlestick(candle, chart_height, min_price, max_price, 2)
            color = curses.color_pair(1) if candle.is_bullish else curses.color_pair(2)
            pad.addstr(row, candle_x, candle_lines[i], color)

def draw_order_book_section(pad, start_row, start_col, symbol, bids, asks, decimals):
    try:
        title = f"Order Book ({symbol})"
        pad.addstr(start_row, start_col, title.center(40), curses.color_pair(3))
        
        max_width = 20

        for i in range(10):
            row = start_row + 1 + i
            if i < len(bids):
                bid_price = float(bids[i][0])
                bid_qty = float(bids[i][1])
                if bid_qty >= 1_000_000:
                    qty_str = f"{bid_qty/1_000_000:.2f}M"
                elif bid_qty >= 1_000:
                    qty_str = f"{bid_qty/1_000:.2f}K"
                else:
                    qty_str = f"{bid_qty:.2f}"
                bid_text = f"{bid_price:>.{decimals}f} ({qty_str})"
                if len(bid_text) > max_width:
                    bid_text = bid_text[:max_width]
                pad.addstr(row, start_col, bid_text, curses.color_pair(1) | curses.A_BOLD)
            
            if i < len(asks):
                ask_price = float(asks[i][0])
                ask_qty = float(asks[i][1])
                if ask_qty >= 1_000_000:
                    qty_str = f"{ask_qty/1_000_000:.2f}M"
                elif ask_qty >= 1_000:
                    qty_str = f"{ask_qty/1_000:.2f}K"
                else:
                    qty_str = f"{ask_qty:.2f}"
                ask_text = f"{ask_price:>.{decimals}f} ({qty_str})"
                if len(ask_text) > max_width:
                    ask_text = ask_text[:max_width]
                pad.addstr(row, start_col + 20, ask_text, curses.color_pair(2) | curses.A_BOLD)
        
        pad.addstr(start_row + 10, start_col, " " * 40, curses.color_pair(3))
    except curses.error:
        pass

def draw_ui(stdscr):
    gc.enable()
    
    curses.start_color()
    curses.init_pair(1, CONFIG['colors']['up'], curses.COLOR_BLACK)
    curses.init_pair(2, CONFIG['colors']['down'], curses.COLOR_BLACK)
    curses.init_pair(3, CONFIG['colors']['neutral'], curses.COLOR_BLACK)
    curses.curs_set(0)

    binance_client = Client()
    okx_client = MarketData.MarketAPI(flag="0")
    bitget_client = BitgetClient()

    chart_section_height = len(tracked_symbols[:8]) * (CONFIG['chart']['height'] + 3)
    author_box_height = 4
    total_height = chart_section_height + author_box_height
    total_width = CONFIG['layout']['padding'] + 70

    pad = curses.newpad(total_height +1, total_width)
    current_scroll = 0

    while True:
        try:
            max_y, max_x = stdscr.getmaxyx()
            max_scroll = total_height - max_y if total_height > max_y else 0

            pad.clear()

            for i, item in enumerate(tracked_symbols[:8]):
                symbol = item["symbol"]
                decimals = item["decimals"]
                exchange = item["exchange"]
                market = item["market"]

                client = okx_client if exchange == "okx" else (bitget_client if exchange == "bitget" else binance_client)
                if i < CONFIG['layout']['items_per_column']:
                    row = author_box_height + (i * (CONFIG['chart']['height'] + 3))
                    col = 0
                else:
                    row = author_box_height + ((i - CONFIG['layout']['items_per_column']) * (CONFIG['chart']['height'] + 3))
                    col = CONFIG['layout']['padding']

                candles = get_candle_data(client, symbol, market, interval='1m', limit=CONFIG['chart']['candles'])
                if candles:
                    bids, asks = get_order_book(client, symbol, market, limit=9)
                    draw_chart_section(pad, row, col, candles, symbol, decimals, exchange, market, CONFIG['chart']['height'])
                    draw_order_book_section(pad, row, col + 30, symbol, bids, asks, decimals)

            author_info = "│ Author: KKKKKCAT │ 🌟 Github: github.com/KKKKKCAT │ 📱 Telegram: @kkkkkcat │ 📦 v1.2.0 │"
            box_width = len(author_info) + 3
            ref_info = "│ 🔗 Register Binance: https://accounts.binance.com/register?ref=MQIXZL5C".ljust(box_width - 2) + "│"
            box_top = "┌" + "─" * (box_width-2) + "┐"
            box_bottom = "└" + "─" * (box_width-2) + "┘"
            
            info_row = 0
            pad.addstr(info_row, 0, box_top, curses.color_pair(3))
            pad.addstr(info_row + 1, 0, author_info, curses.color_pair(3))
            pad.addstr(info_row + 2, 0, ref_info, curses.color_pair(3))
            pad.addstr(info_row + 3, 0, box_bottom, curses.color_pair(3))

            stdscr.nodelay(1)
            key = stdscr.getch()
            scroll_speed = 15
            if key == ord('k') and current_scroll > 0:
                current_scroll = max(0, current_scroll - scroll_speed)
            elif key == ord('j') and current_scroll < max_scroll:
                current_scroll = min(max_scroll, current_scroll + scroll_speed)
            elif key == ord('q'):
                break

            pad.refresh(current_scroll, 0,
                       0, 0,
                       min(max_y - 1, total_height),
                       min(max_x - 1, total_width - 1))

            time.sleep(CONFIG['chart']['refresh_rate'])
            
        except curses.error:
            continue

    return
          
if __name__ == "__main__":
  curses.wrapper(draw_ui)

