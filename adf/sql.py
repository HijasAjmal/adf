"""
SQL Query interface for adf.
"""
from collections import OrderedDict
from adf.core import Adf
from adf import readers
from adf.utils import *

def select(df,
           cols=["*"]):
        """
        This is really naive implementation of select. takes df and cols as input
        and select columns which are listed in "cols", also accept * wildcard.
        Memory management is still an issue as if data is too large data_subset might blow up(or out).

        :return:
        """
        valid_col_signs = ["*"]

        if len(cols) == 1 and cols[0] in valid_col_signs:
            return df
        elif len(cols) == 0:
            print("Not a valid column")
        else:
            new_df = Adf(readers.base_reader)
            data_subset = {k: df.data[k] for k in df.data if k in cols}
            new_df.read(data_subset)
            return new_df

def where():
    pass

def groupby():
    pass

def orderby():
    pass

def map():
    pass

def reduce():
    pass
