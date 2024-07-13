import streamlit as st

# Judul utama dari website
st.title("Sistem Kontrol Suhu Pada Alat Pengering Gabah")
st.image("./mesin-dryer.jpg")

button1_state = False

# Topik pertama
st.header("Pilih Data")

def show_images():
    tab1.image("./kurva_suhu.png")
    # state = 1
    # if state == 1: 
    #     tab1.image("./kurva_suhu.png")
    # elif state == 0: 
    #     pass

tab1, tab2 = st.tabs(["Suhu vs Waktu","Suhu vs Kecepatan Angin"])

tab1.button("Tampilkan Gambar!", on_click = show_images())# and not button1_state: 
#     button1_state = True
# tab1.button("Sembunyikan Gambar!", on_click = show_images()) #and button1_state:
#     button1_state = False

tab2.link_button("Menuju ke google","https://www.google.co.id")




