"""
Deep-time Data Optimizer
Helps Earth scientists improve the discoverability and readability of their data.
"""

import streamlit as st
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from utils.optimizer import optimize_dataframe

st.set_page_config(
    page_title="Deep-time Data Optimizer",
    page_icon="🔍",
    layout="wide",
)

st.title("Deep-time Data Optimizer")
st.caption("深时科学数据检索优化器 · Improve metadata for better discovery, understanding, and citation")

st.markdown("""
Upload a CSV containing deep-time records. The tool will assess completeness of key fields,
suggest improvements, and generate structured summaries that are easier for both humans and AI systems to use.
""")

uploaded = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded is not None:
    try:
        df = pd.read_csv(uploaded)
        st.subheader("Original data preview")
        st.dataframe(df.head(10), use_container_width=True)

        optimized = optimize_dataframe(df)

        st.subheader("Optimized data")
        st.dataframe(optimized, use_container_width=True)

        # Summary statistics
        avg_score = optimized["completeness_score"].mean()
        st.metric("Average completeness score", f"{avg_score:.2f}")

        st.subheader("Download optimized dataset")
        csv = optimized.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download optimized CSV",
            data=csv,
            file_name="optimized_deep_time_data.csv",
            mime="text/csv",
        )

        with st.expander("What was added"):
            st.markdown("""
            - **completeness_score**: Fraction of essential fields that are filled (0–1).
            - **improvement_suggestions**: Concrete recommendations for missing or weak metadata.
            - **structured_summary**: A short natural-language description of the record.
            - **optimized_for_retrieval**: Flag indicating the record has been processed.
            """)

    except Exception as e:
        st.error(f"Could not process the file: {e}")
else:
    st.info("Please upload a CSV file to begin. A minimal example can include columns such as name, age_ma, locality, lithology, taxon_or_unit, and reference.")

st.divider()
st.caption(
    "This optimizer focuses on practical metadata improvements commonly needed for deep-time scientific data. "
    "It is intended as a supporting tool within the Deep-time Observatory (DDE) framework. "
    "Always verify suggestions against authoritative sources and domain expertise."
)
