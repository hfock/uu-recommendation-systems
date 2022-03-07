# Import
import pandas as pd
import streamlit as st
from constant import DATA

# import own files
import model
import view


class Controller:

    def __init__(self, streamlit, ):
        self.md = model.Model(streamlit)
        self.vw = view.View(streamlit)


if __name__ == '__main__':
    ct = Controller(st)
    md = ct.md
    vw = ct.vw

    vw.sidebar()

    pd_books = model.load(f'{DATA}BX-Books.csv')
    most_reviewed = model.load(f'{DATA}recommendations/recommendations-most-reviewed.csv')

    vw.most_reviewed(most_reviewed, pd_books)
