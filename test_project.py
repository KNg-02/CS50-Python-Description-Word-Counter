#Import 3 functions from the project.py file to test!
#from project import filtered_dataframe
import project

#Note: Dataframes prefer to use assert_frame_equal() as their own version of pytest,
#if nothing happens upon the test function being called, it means that there's no error
from pandas.testing import assert_frame_equal

import pandas as pd # type: ignore

#Import dataframe
DF = pd.read_csv('cookie1.csv', encoding='latin-1')
DF_2 = pd.read_csv('cookie1_assert_dataframe_test.csv', encoding='utf-8-sig')
DF_3 = pd.read_csv('cookie1_assert_word_counter.csv', encoding='utf-8-sig')
DF_4 = pd.read_csv('cookie1_assert_length_descending.csv', encoding='utf-8-sig')

#Convert year to string
DF['year'] = DF['year'].map(str)

DF_2['year'] = DF_2['year'].map(str)

DF_3['year'] = DF_3['year'].map(str)
#DF_3['length'] = DF_3['length'].map(str)

DF_4['year'] = DF_4['year'].map(str)

def test_counter_DF_filter():
    assert_frame_equal(project.counter_DF_filter(['rarity'], [['Ancient']], DF), DF_2)

def test_word_counter():
    assert_frame_equal(project.word_counter(DF_2), DF_3)

def test_length_descending():
    assert_frame_equal(project.length_descending(DF_3), DF_4)

test_counter_DF_filter()
test_word_counter()
test_length_descending()
