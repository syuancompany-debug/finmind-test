from FinMind.data import DataLoader

FM = DataLoader()

df = FM.taiwan_stock_daily(
    stock_id="0050",
    start_date="2020-01-01",
    end_date="2022-01-01",
)

print(df.head())
print(df.tail())
print(df.shape)
