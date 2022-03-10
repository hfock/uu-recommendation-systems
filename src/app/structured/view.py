import constant as c
import streamlit as st

from CurrentShow import CurShow

from random import random


def display_selected_item_advanced(cur_show: CurShow):
    # create a cover and info column to display the selected book
    cover, info = st.columns([2, 2])

    with cover:
        # display the image
        st.image(cur_show.image_l)

    with info:
        # display the book information
        st.title(cur_show.title)
        st.caption(cur_show.desc)
        st.caption(f'Category: {cur_show.category}')
        st.caption(cur_show.keywords)

    with st.expander("Synopses"):
        st.text(cur_show.syno_l)


def recommendations(df):
    # check the number of items
    nbr_items = df.shape[0]

    if nbr_items != 0:
        # create columns with the corresponding number of items
        columns = st.columns(nbr_items)

        # convert df rows to dict lists
        items = df.to_dict(orient='records')
        # apply tile_item to each column-item tuple (created with python 'zip')
        any(tile_item(x[0], x[1]) for x in zip(columns, items))


def tile_item(column, item):
    with column:
        st.button('📖', key=random(), on_click=select_show, args=(item['index'],))
        st.image(item['image_l'], use_column_width='always')
        st.caption(item['title'])


def select_show(id):
    print(f'input value is {id}')
    st.session_state[c.ID] = id


def sidebar():
    with st.sidebar:
        st.session_state[c.CPLXTY_MODE] = st.selectbox('User Mode', [c.DEFAULT, c.ADVANCED])

        if st.session_state[c.CPLXTY_MODE] == c.ADVANCED:
            pass


def make_markdown_iteration(values):
    result = ''
    for value in values.split(', '):
        result = result + '\n- ' + value
    return result
