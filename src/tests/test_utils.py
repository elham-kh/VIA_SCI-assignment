from src.utils import *
import pytest

# test the csv reader function
def test_csv_read():
    x, y = csv_reader('test-data.csv')
    assert x[1][1] == 1.68, 'csv file read failed'
    assert y[0][0] == 32, 'csv file read failed'
    assert (float(x[0][0])+float(x[1][0]))/2 == 35.5, 'csv file read failed'

# test the histogram generator function
def test_histogram():
    x, y = csv_reader('test-data.csv')
    counts_x, bin_edges_x, counts_y, bin_edges_y, column_width = calculate_histogram(x,y)
    assert counts_x[0] == 2, 'histogram calculation failed'
    assert bin_edges_y[1] == 2.3256, 'histogram calculation failed'
