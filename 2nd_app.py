import streamlit as st

tab1, tab2 = st.tabs(["Tab1","Tab2"])

tab1.write("Ini tab 1!")
tab1.image("./mesin-dryer.jpg")


tab2.write("Ini tab 2!")
tab2.button("Reset", type="primary")
if tab2.button("Say hello"):
    tab2.write("Why hello there")
else:
    tab2.write("Goodbye")


# st.image("./mesin-dryer.jpg")