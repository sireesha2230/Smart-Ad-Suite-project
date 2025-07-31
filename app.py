# app.py

import streamlit as st
import pandas as pd
from optimizer import optimize_budget
from ad_generator import generate_ad_copy

st.set_page_config(page_title="SmartAd Suite", layout="wide")
st.title("🚀 SmartAd Suite – AI Ad Campaign Toolkit")

st.sidebar.header("1️⃣ Ad Budget Optimizer")
total_budget = st.sidebar.slider("Total Budget (₹)", 100, 100000, 1000)
uploaded_file = st.sidebar.file_uploader("Upload Ad Metrics CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    result_df = optimize_budget(total_budget, df)
    st.subheader("📊 Optimized Budget Allocation")
    st.dataframe(result_df)
    st.bar_chart(result_df.set_index("Platform"))

st.sidebar.markdown("---")
st.sidebar.header("2️⃣ Ad Copy Generator (OpenAI GPT-3.5)")

api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
product = st.sidebar.text_area("Product / Service Description")
platform = st.sidebar.selectbox("Platform", ["Google", "Facebook", "LinkedIn"])
tone = st.sidebar.selectbox("Ad Tone", ["Professional", "Friendly", "Funny", "Persuasive"])

if st.sidebar.button("Generate Ad Copy"):
    if api_key and product:
        try:
            ad_copy = generate_ad_copy(product, tone, platform, api_key)
            st.subheader("✍️ Generated Ad Copy")
            st.code(ad_copy)
        except Exception as e:
            st.error(f"Error generating ad copy: {e}")
    else:
        st.warning("Please provide both API key and product description.")
