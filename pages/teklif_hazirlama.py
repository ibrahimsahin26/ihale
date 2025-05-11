
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Teklif Hazırlama Modülü", layout="wide")

st.markdown("### 📝 Teklif Hazırlama Modülü")

st.subheader("ℹ️ İhale Bilgileri")
col1, col2, col3 = st.columns(3)
ihale_adi = col1.text_input("İhale Adı")
ihale_tarihi = col2.date_input("İhale Tarihi", date.today())
kurum_adi = col3.text_input("Kurum Adı")

st.subheader("📦 Ürün Listesi")
uploaded_file = st.file_uploader("Excel dosyası yükleyin (ad, birim, teknik özellik, fiyat vb.)", type=["xlsx", "xls"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Dosya okunamadı: {e}")
else:
    st.info("Ürün listesini içeren bir Excel dosyası yükleyin.")
