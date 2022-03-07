import streamlit as st
import pandas as pd
import template as t
import default_page as dp

# Constants
from constant import CPLXTY, DVRSTY

if __name__ == '__main__':
    st.set_page_config(layout="wide")

    df_books = pd.read_csv('./BX-Books.csv', sep=';', encoding='latin-1')

    if CPLXTY not in st.session_state:
        st.session_state[CPLXTY] = 'Default'

    if DVRSTY not in st.session_state:
        st.session_state[DVRSTY] = 'Diversity'

    with st.sidebar:
        st.session_state[CPLXTY] = st.radio(CPLXTY, ['Default', 'Advanced'])
        st.session_state[DVRSTY] = st.radio(DVRSTY, ['Low', 'Mid', 'High'])
        st.selectbox('Mood for different', ['cats', 'dogs'])


