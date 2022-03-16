# Import
import pandas as pd
import streamlit as st
import constant as c

# import own files
import model as md
import view as vw

from CurrentShow import CurShow


@st.cache
def load_data():
    bbc_dataframe = pd.read_csv(f'{c.DATA_BBC}bbc_data_slim.csv', delimiter=',')
    bbc_table_view_dataframe = pd.read_csv(f'{c.DATA_BBC}bbc_data_adv.csv', index_col=0, delimiter=';')
    bbc_cosin_sim = pd.read_csv(f'{c.DATA_BBC}cosine_similarity.csv', index_col=0, delimiter=';')

    return bbc_dataframe, bbc_table_view_dataframe, bbc_cosin_sim


def entry_by_id(df_input: pd.DataFrame, id_input: int):
    return df_input[df_input[c.ID] == id_input].iloc[0]


def page_load():
    if st.session_state[c.MODE] == c.EXPLORE:
        cur_show = CurShow(entry_by_id(df, st.session_state[c.ID]))
        vw.display_selected_item_advanced(cur_show)

        number_of_items = 8
        recom_entries = df.iloc[sim_title(df_cosin, st.session_state[c.ID], number_of_items), :]
        vw.recommendations(recom_entries,
                           'Recommendations based on the movie you just watched')

        # recom_on_genre = df.iloc[sim_title_by_genre(df, df_cosin, st.session_state[c.ID], number_of_items)]
        # vw.recommendations(recom_on_genre,
        #                    'Recommendations based on the selected genre')

        if not st.session_state[c.PRIVACY]:
            hist_recom_entries = df.iloc[sim_title_by_many(df_cosin, st.session_state[c.HISTORY], number_of_items)]
            vw.recommendations(hist_recom_entries,
                               'Recommendations based on your history')
    elif st.session_state[c.MODE] == c.ADVANCED:
        vw.exploration(df_adv)

    elif st.session_state[c.MODE] == c.HISTORY:
        if st.session_state[c.HISTORY]:
            for entry_id in st.session_state[c.HISTORY][::-1]:
                vw.display_selected_item_advanced(CurShow(entry_by_id(df, entry_id)))
        else:
            st.write('No History yet')
    else:
        st.session_state[c.MODE] = c.EXPLORE


def sim_title(df_cosin_similarity, index: int, number_of_recom):
    recoms = df_cosin_similarity.loc[index].sort_values(ascending=False).index.tolist()[1:number_of_recom]
    return list(map(int, recoms))


def sim_title_by_many(df_cosin_similarity, indices: list, number_of_recom):
    combined = df_cosin_similarity.iloc[:, indices]
    combined['combined'] = combined.mean(axis=1)
    combined = combined.drop(st.session_state[c.HISTORY], axis=0)
    recoms = combined['combined'].sort_values(ascending=False).index.tolist()[1:number_of_recom]
    return list(map(int, recoms))


def sim_title_by_genre(df, df_cosin_similarity, index, number_of_recom):
    fitting_genre = df[df['category'] == st.session_state[c.GENRE]]
    print(len(fitting_genre))
    df_cosin_genre_exc = df_cosin_similarity.iloc[[fitting_genre.index, index]]
    recoms = df_cosin_genre_exc.loc[index].sort_values(ascending=False).index.tolist()[1:number_of_recom]
    return list(map(int, recoms))


if __name__ == '__main__':
    st.set_page_config(layout="wide")

    # init session keys
    md.init_session_keys()

    # load data
    df, df_adv, df_cosin = load_data()

    vw.sidebar(df)

    page_load()




