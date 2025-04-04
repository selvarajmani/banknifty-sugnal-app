import streamlit as st
import datetime

# ----------- Demo Inputs ----------- #
st.title("📈 BankNIFTY Trading Signal App")

st.markdown("Made with ❤️ for Selva")

# Input Fields
strike = st.selectbox("Select ATM Strike Price", [45200, 45300, 45400, 45500])
spot_price = st.number_input("Spot Price", value=45350)
ce_volume = st.number_input("CE Volume", value=120000)
pe_volume = st.number_input("PE Volume", value=180000)
ce_ltp = st.number_input("CE LTP", value=85.5)
pe_ltp = st.number_input("PE LTP", value=120.7)

# Timestamp
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ----------- Logic ----------- #
signal = "Avoid"
confidence = "⚠️ Weak Signal"
reason = ""

if pe_volume - ce_volume > 40000 and pe_ltp > ce_ltp and spot_price < strike:
    signal = "Buy PE"
    confidence = "✅ Confirmed"
    reason = "PE Volume Spike + Spot Drop"
elif ce_volume - pe_volume > 40000 and ce_ltp > pe_ltp and spot_price > strike:
    signal = "Buy CE"
    confidence = "✅ Confirmed"
    reason = "CE Volume Spike + Spot Rise"

# ----------- Output ----------- #
st.markdown("---")
st.subheader(f"🕒 {time}")
st.markdown(f"### 🔍 Signal: **{signal}**")
st.markdown(f"**Confidence:** {confidence}")
if reason:
    st.markdown(f"**Reason:** {reason}")

st.markdown("---")
st.caption("This is a basic prototype. We can add live data, scoring logic, charts, and alerts next!")