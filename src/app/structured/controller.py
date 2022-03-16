# Import
import pandas as pd
import streamlit as st
import constant as c

# import own files
import model as md
import view as vw

from CurrentShow import CurShow


def entry_by_id(df_input: pd.DataFrame, id_input: int):
    return df_input[df_input[c.ID] == id_input].iloc[0]


def page_load():
    if st.session_state[c.MODE] == c.ADVANCED:
        vw.exploration(df_adv)

    elif st.session_state[c.MODE] == c.HISTORY:
        if st.session_state[c.HISTORY]:
            for entry_id in st.session_state[c.HISTORY][::-1]:
                vw.display_selected_item_advanced(CurShow(entry_by_id(df, entry_id)))
        else:
            st.write('No History yet')

    elif st.session_state[c.MODE] == c.EXPLORE:
        cur_show = CurShow(entry_by_id(df, st.session_state[c.ID]))
        vw.display_selected_item_advanced(cur_show)

        vw.recommendations(df.iloc[0:6])
    else:
        st.session_state[c.MODE] = c.EXPLORE


@st.cache
def load_data():
    bbc = md.load_csv(f'{c.DATA_BBC}bbc_data.csv', delimiter=';')
    bbc_images = md.load_csv(f'{c.DATA_BBC}bbc_images.csv', delimiter=';')
    df = bbc.merge(bbc_images, on='index')
    df_adv = md.load_csv(f'{c.DATA_BBC}bbc_data_adv.csv', delimiter=';', index_col=0)

    return df, df_adv


if __name__ == '__main__':
    st.set_page_config(layout="wide")

    # init session keys
    md.init_session_keys()

    # load data
    df, df_adv = load_data()

    vw.sidebar()

    page_load()




