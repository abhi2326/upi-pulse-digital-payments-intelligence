from pathlib import Path
import argparse
import numpy as np
import pandas as pd

def generate(rows=12000, seed=42):
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2024-01-01", periods=730, freq="D")
    n = rows
    ts = pd.to_datetime(rng.choice(dates, n)) + pd.to_timedelta(rng.integers(0, 86400, n), unit="s")
    amount = np.round(rng.lognormal(5.0, 1.0, n), 2)
    city = rng.choice(["Bengaluru","Mumbai","Delhi","Hyderabad","Pune","Lucknow","Jaipur","Chennai"], n)
    segment = rng.choice(["Micro","Small","Medium","Enterprise"], n, p=[.42,.34,.19,.05])
    category = rng.choice(["Grocery","Electronics","Fashion","Food","Mobility","Healthcare","Other"], n)
    data = {"record_id": np.arange(1,n+1), "event_time": ts, "city": city,
            "segment": segment, "category": category, "amount": amount}
    return pd.DataFrame(data)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--rows",type=int,default=12000)
    p.add_argument("--output",default="data/raw/demo.csv")
    a=p.parse_args()
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True)
    df=generate(a.rows); df.to_csv(out,index=False)
    print(f"Wrote {len(df):,} SYNTHETIC demo rows to {out}")
if __name__=="__main__": main()
