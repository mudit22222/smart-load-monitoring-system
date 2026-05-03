import streamlit as st
import sqlite3
import pandas as pd
import time

# ─── Page Config ─────────────────────────────────────────────
st.set_page_config(
    page_title="Smart Load Monitor",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Smart Electrical Load Monitoring Dashboard")

# ─── Load Data from Database ──────────────────────────────────
def load_data():
    try:
        conn = sqlite3.connect('energy_data.db')
        df = pd.read_sql_query(
            "SELECT * FROM energy_logs ORDER BY timestamp DESC LIMIT 100",
            conn
        )
        conn.close()
        return df
    except Exception as e:
        st.error(f"Database error: {e}")
        return pd.DataFrame()  # return empty if DB not ready

# ─── Auto Refresh Every 5 Seconds ────────────────────────────
refresh = st.sidebar.slider("Auto-refresh every (seconds)", 2, 30, 5)
placeholder = st.empty()

while True:
    df = load_data()

    with placeholder.container():

        if df.empty:
            st.warning("No data yet. Waiting for ESP32 to send readings...")

        else:
            # Reverse so chart shows oldest → newest (left to right)
            df_chart = df[::-1].reset_index(drop=True)

            # ─── Summary Cards ───────────────────────────────
            col1, col2, col3 = st.columns(3)
            col1.metric("🔋 Latest Voltage",  f"{df['voltage'].iloc[0]:.2f} V")
            col2.metric("⚡ Latest Current",  f"{df['current'].iloc[0]:.2f} A")
            col3.metric("💡 Latest Power",    f"{df['power'].iloc[0]:.2f} W")

            # ─── Line Charts ─────────────────────────────────
            st.subheader("📈 Voltage over Time")
            st.line_chart(df_chart['voltage'])

            st.subheader("📈 Current over Time")
            st.line_chart(df_chart['current'])

            st.subheader("📈 Power over Time")
            st.line_chart(df_chart['power'])

            # ─── Data Table ──────────────────────────────────
            st.subheader("🗃️ Latest 10 Readings")
            st.dataframe(
                df.head(10)[['timestamp', 'voltage', 'current', 'power']],
                use_container_width=True
            )

    time.sleep(refresh)
