# Import
import pandas as pd
import streamlit as st
import constant as c

# import own files
import model as md
import view as vw

from CurrentShow import CurShow

if __name__ == '__main__':
    print('Refresh')
    st.set_page_config(layout="wide")

    bbc = md.load_csv(f'{c.DATA_BBC}bbc_data.csv', delimiter=';')
    bbc_images = md.load_csv(f'{c.DATA_BBC}bbc_images.csv', delimiter=';')
    df = bbc.merge(bbc_images, on='index')

    md.init_session_keys()

    print(f'Session state id {st.session_state[c.ID]}')
    cur_show = CurShow(df[df[c.ID] == st.session_state[c.ID]].iloc[0])
    vw.display_selected_item_advanced(cur_show)
    vw.sidebar()

    vw.recommendations(df.iloc[0:6])
