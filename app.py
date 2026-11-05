import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
st.set_page_config(page_title="Business Intelligence",layout="wide")
st.title("UPI Pulse: India's Digital Payments Intelligence Platform")
st.caption("Synthetic portfolio dataset — replace with licensed/public source data for empirical findings.")
f=Path("data/processed/clean.csv")
if not f.exists():
    st.warning("Run: python -m src.generate_data && python -m src.pipeline")
    st.stop()
df=pd.read_csv(f,parse_dates=["event_time"])
a,b,c,d=st.columns(4)
a.metric("Records",f"{len(df):,}")
b.metric("Total value",f"₹{df.amount.sum():,.0f}")
c.metric("Average value",f"₹{df.amount.mean():,.0f}")
d.metric("Cities",df.city.nunique())
left,right=st.columns(2)
with left:
    st.plotly_chart(px.line(df.groupby("month",as_index=False).amount.sum(),x="month",y="amount",title="Monthly transaction value"),use_container_width=True)
with right:
    st.plotly_chart(px.bar(df.groupby("city",as_index=False).amount.sum().sort_values("amount",ascending=False),x="city",y="amount",title="Value by city"),use_container_width=True)
st.plotly_chart(px.box(df,x="segment",y="amount",title="Value distribution by segment"),use_container_width=True)
st.subheader("Business questions to investigate")
st.markdown("- Which segments and locations explain most of the value?\n- Where do operational failures or drop-offs concentrate?\n- Which cohorts, categories or periods deserve deeper investigation?")
st.dataframe(df.head(100),use_container_width=True)
