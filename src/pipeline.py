from pathlib import Path
import pandas as pd
import numpy as np

def run(input_path="data/raw/demo.csv", output_path="data/processed/clean.csv"):
    df=pd.read_csv(input_path, parse_dates=["event_time"])
    df=df.drop_duplicates("record_id").copy()
    df["amount"]=pd.to_numeric(df["amount"], errors="coerce")
    df=df[df["amount"].notna() & (df["amount"]>=0)]
    df["month"]=df["event_time"].dt.to_period("M").astype(str)
    df["weekday"]=df["event_time"].dt.day_name()
    df["hour"]=df["event_time"].dt.hour
    df["amount_band"]=pd.cut(df["amount"],[-1,500,2000,10000,float("inf")],
                             labels=["0-500","500-2K","2K-10K","10K+"])
    Path(output_path).parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(output_path,index=False)
    return df
if __name__=="__main__":
    d=run(); print(d.describe(include="all").to_string())
