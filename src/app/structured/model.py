from constant import CPLXTY, DVRSTY
import pandas as pd


def load(csv_path) -> pd.DataFrame:
    return pd.read_csv(csv_path, sep=';', encoding='latin-1')


class Model:
    def __init__(self, streamlitObject):
        self.st = streamlitObject
        self.st.session_state[CPLXTY] = CPLXTY
        self.st.session_state[DVRSTY] = DVRSTY
