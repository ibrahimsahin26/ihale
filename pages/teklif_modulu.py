import streamlit as st
import pandas as pd

st.set_page_config(page_title="Teklif Modülü", layout="wide")
st.title("📄 Teklif Hazırlama Modülü")

uploaded_file = st.file_uploader("Excel dosyası yükleyin", type=["xlsx", "xls"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("Dosya başarıyla yüklendi.")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Hata oluştu: {e}")
else:
    st.info("Ürün listesini içeren bir Excel dosyası yükleyin.")
