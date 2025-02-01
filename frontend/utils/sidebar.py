import streamlit as st


def show_sidebar():
    # Agregar un título en la sidebar
    st.sidebar.header(":green[Eye]Fraud 💵", divider="green")

    # Enlaces a otras páginas (si usas el sistema de páginas de Streamlit)
    st.sidebar.page_link("pages/1_📊_analysis.py", label="📊 Análisis de datos")
    st.sidebar.page_link("pages/2_🔍_prediction.py",
                         label="🔍 Predicción de datos")
    st.sidebar.page_link("pages/3_📩_contact.py", label="📩 Contacto")

    st.sidebar.header("Equipo 🤝", divider="green")
    st.sidebar.subheader(":orange[C23-116-Data]")

    st.sidebar.link_button(label="Proyecto en GitHub",
                           url="https://github.com/No-Country-simulation/c23-116-data")
