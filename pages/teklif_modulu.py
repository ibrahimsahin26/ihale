
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Teklif Modülü", layout="wide")

st.markdown("## 📝 Teklif Hazırlama Modülü")

# İhale Bilgileri
st.markdown("### ℹ️ İhale Bilgileri")
col1, col2, col3 = st.columns(3)
with col1:
    ihale_adi = st.text_input("İhale Adı")
with col2:
    ihale_tarihi = st.date_input("İhale Tarihi")
with col3:
    kurum_adi = st.text_input("Kurum Adı")

# İhale Türü Seçimi
st.markdown("### 🔄 İhale Türü Seçiniz")
ihale_turu = st.radio(
    "İhale Türü",
    ["Açık İhale", "Doğrudan Temin - E-Teklif", "Doğrudan Temin - PDF"],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()

# Excel yükleme
st.markdown("### 📦 Ürün Listesi Yükle")
yuklenen_dosya = st.file_uploader("Excel dosyası yükleyin", type=["xlsx", "xls"], label_visibility="collapsed")

if yuklenen_dosya:
    df = pd.read_excel(yuklenen_dosya)
    st.dataframe(df, use_container_width=True)

    st.divider()
    if ihale_turu == "Açık İhale":
        st.success("Açık İhale formatı seçildi. EKAP uyumlu Excel çıktısı alabilirsiniz.")
        st.download_button("📥 Excel Çıktısı", df.to_csv(index=False).encode("utf-8"), file_name="acik_ihale_teklif.csv", mime="text/csv")

    elif ihale_turu == "Doğrudan Temin - E-Teklif":
        st.success("E-Teklif formatı seçildi. Kurumsal bilgilerle birlikte Excel oluşturulacak.")
        st.download_button("📥 E-Teklif Excel", df.to_csv(index=False).encode("utf-8"), file_name="eteklif_teklif.csv", mime="text/csv")

    elif ihale_turu == "Doğrudan Temin - PDF":
        st.success("PDF formatı seçildi. Teklif belgesi oluşturulacak.")
        st.button("📄 PDF Teklif Oluştur (Beta)")
else:
    st.info("Ürün listesi içeren bir Excel dosyası yükleyin.")
