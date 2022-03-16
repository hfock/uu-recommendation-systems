import constant as c
import streamlit as st
import pandas as pd


from CurrentShow import CurShow, CurShowJson

from random import random

from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode


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
        st.button('🕶', key=random(), on_click=select_show, args=(item['index'],))
        st.image(item['image_l'], use_column_width='always')
        st.caption(item['title'])


def select_show(id):
    print(f'input value is {id}')
    st.session_state[c.HISTORY].append(id)
    st.session_state[c.ID] = id


def sidebar():
    st.session_state[c.MODE] = st.sidebar.radio('Go To', [c.EXPLORE, c.ADVANCED, c.HISTORY])
    st.sidebar.info('This is a mid-fidelity prototype. It is not possible to play any video.')


def make_markdown_iteration(values):
    result = ''
    for value in values.split(', '):
        result = result + '\n- ' + value
    return result


def exploration(df_adv, ):
    selection = aggrid_interactive_table(df_adv)
    if selection:
        if selection["selected_rows"]:
            sel_show = CurShowJson(selection["selected_rows"][0])
            st.session_state[c.ID] = sel_show.index
            st.markdown(f'''
            ## {sel_show.title}
            > {sel_show.desc}
            ***
            Category **{sel_show.category}** produced from the channel **{sel_show.channel}**
            
            Duration **{sel_show.duration} Minutes**
            ''')

            st.write('To watch the movie click the glasses')
            if st.button('🕶'):
                st.session_state[c.MODE] = c.EXPLORE
                st.session_state[c.HISTORY].append(sel_show.index)


def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.
    Args:
        df (pd.DataFrame]): Source dataframe
    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )
    return selection
