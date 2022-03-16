import constant as c
import streamlit as st
import pandas as pd


def init_session_keys():
    if c.ID not in st.session_state:
        st.session_state[c.ID] = 1
    if c.MODE not in st.session_state:
        st.session_state[c.MODE] = c.EXPLORE
    if c.HISTORY not in st.session_state:
        st.session_state[c.HISTORY] = []


# latin-1
def load_csv(csv_file_path, delimiter=',', index_col=None, encoding='utf8', low_memory=True):
    return pd.read_csv(csv_file_path,
                       delimiter=delimiter,
                       encoding=encoding,
                       index_col=index_col,
                       low_memory=low_memory)


def save_csv(df, csv_file_path, index=False):
    df.to_csv(csv_file_path, index=index)
