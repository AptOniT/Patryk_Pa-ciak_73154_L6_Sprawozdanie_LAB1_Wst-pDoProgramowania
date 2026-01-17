import numpy as np
import pandas as pd
rng = np.random.default_rng(42)
dates = pd.date_range("2024-01-01", periods=120, freq="D")
kraj = rng.choice(["PL", "DE", "US"], size=len(dates))
sprzedaz = rng.integers(50, 250, size=len(dates))
koszt = sprzedaz * rng.uniform(0.4, 0.8, size=len(dates))
produkt = rng.choice(["A", "B", "C"], size=len(dates))
df = pd.DataFrame({
"Data": dates,
"Kraj": kraj,
"Produkt": produkt,
"Sprzedaż": sprzedaz,
"Koszt": np.round(koszt, 2),
"Waluta": "PLN"

})
df['Marża'] = df['Sprzedaż'] - df['Koszt']
df.head()
print(df)
