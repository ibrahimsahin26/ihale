
import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Teklif Hazırlama Modülü", layout="wide")
st.title("📄 Teklif Hazırlama Modülü")

# --- Teklif Genel Bilgileri ---
st.subheader(":information_source: İhale Bilgileri")
col1, col2, col3 = st.columns(3)
with col1:
    ihale_adi = st.text_input("İhale Adı")
with col2:
    ihale_tarihi = st.date_input("İhale Tarihi", value=datetime.date.today())
with col3:
    kurum_adi = st.text_input("Kurum Adı")

# --- Ürün Yükleme veya Seçme ---
st.subheader(":package: Ürün Listesi")
dosya = st.file_uploader("Excel dosyası yükleyin (ad, birim, teknik özellik, fiyat vb.)", type=["xlsx", "xls"])

if dosya:
    try:
        df = pd.read_excel(dosya)
        st.success(f"{df.shape[0]} satır yüklendi.")

        # Kolon isimlerini göster ve gerekli alanları seçtir
        kolonlar = df.columns.tolist()
        with st.expander("Ürün Bilgisi Eşleştirme"):
            ad_kolon = st.selectbox("Ürün Adı Kolonu", kolonlar)
            birim_kolon = st.selectbox("Birim Kolonu", kolonlar)
            fiyat_kolon = st.selectbox("Alış Fiyatı Kolonu", kolonlar)
            kar_orani = st.number_input("Kar Marjı (%)", min_value=0, max_value=100, value=20)

        # Satış fiyatı hesaplama
        df['Satış Fiyatı'] = df[fiyat_kolon] * (1 + kar_orani / 100)

        # Özet tablo
        st.subheader(":memo: Teklif Tablosu")
        st.dataframe(df[[ad_kolon, birim_kolon, fiyat_kolon, 'Satış Fiyatı']], use_container_width=True)

        # Çıktı formatları
        st.subheader(":outbox_tray: Teklif Çıktısı")
        colpdf, colexcel = st.columns(2)
        with colpdf:
            st.button("PDF Teklif Oluştur")  # Placeholder
        with colexcel:
            st.download_button(
                label="Excel Teklif İndir",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name="teklif_listesi.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"Dosya okunamadı: {e}")
else:
    st.info("Ürün listesini içeren bir Excel dosyası yükleyin.")
