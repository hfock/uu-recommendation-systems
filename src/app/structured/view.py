from constant import CPLXTY, DVRSTY
import pandas as pd

from random import random


class View:
    def __init__(self, streamlitObject):
        self.st = streamlitObject

    def recommendations(self, df):
        # check the number of items
        nbr_items = df.shape[0]

        if nbr_items != 0:
            # create columns with the corresponding number of items
            columns = self.st.columns(nbr_items)

            # convert df rows to dict lists
            items = df.to_dict(orient='records')

            # apply tile_item to each column-item tuple (created with python 'zip')
            any(self.tile_item(x[0], x[1]) for x in zip(columns, items))

    def tile_item(self, column, item):
        with column:
            self.st.button('📖', key=random(), on_click=self.select_book, args=(item['ISBN'],))
            self.st.image(item['Image-URL-M'], use_column_width='always')
            self.st.caption(item['Book-Title'])

    # set episode session state
    def select_book(self, isbn):
        self.st.session_state['ISBN'] = isbn

    def diversity_filter(self):
        pass
        # if self.st.session_state[DVRSTY] == 'Low':
        # apply this
        #   pass
        # else:
        # apply that
        #   with self.st.expander("Recommendations based most reviewed"):
        #      self.most_reviewed(df_book)

    def sidebar(self):
        with self.st.sidebar:
            self.st.session_state[CPLXTY] = self.st.radio(CPLXTY, ['Default', 'Advanced'])
            self.st.session_state[DVRSTY] = self.st.radio(DVRSTY, ['Low', 'Mid', 'High'])
            self.st.selectbox('Mood for different', ['cats', 'dogs'])

    def most_reviewed(self, df_books: pd.DataFrame, most_reviewed: pd.DataFrame):
        df = most_reviewed
        df = df.merge(df_books, on='ISBN')
        self.recommendations(df)

