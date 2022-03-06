import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-BTC", interval="day", count=365)

df['ma5'] = df['close'].rolling(15).mean().iloc[-1]
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)
df['bull'] = df['open'] > df['ma5']

fee = 0.0005
df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                      df['close'] / df['target'] - fee,
                      1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD: ", df['dd'].max())
print("HPR: ", df['hpr'][-2])

print(df)

# df.to_excel("larry_ma.xlsx")

# def get_ma15(ticker):
#     """15일 이동 평균선 조회"""
#     df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
#     ma15 = df['close'].rolling(15).mean().iloc[-1]
#     return ma15
