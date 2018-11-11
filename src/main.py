#from src.utils import get_split_line
from utils import *
import numpy as np
import matplotlib.pyplot as plt
import csv


def main():

    # read csv file and extract data for female and male
    female_data, male_data = csv_reader('../data/data.csv')

    # plot age data
    histogram_plot([row[0] for row in female_data],[row[0] for row in male_data],'women\'s age','men\'s age','age.png')

    # plot height data
    histogram_plot([row[1] for row in female_data],[row[1] for row in male_data],'women\'s height','men\'s height','height.png')

# function to read csv files and assign data to separate lists for female and male
def csv_reader(file_name):
    female_data = []
    male_data = []
    with open(file_name, mode='r') as csv_file:
        csv_data = csv.reader(csv_file)
        header = next(csv_data)     # skip the file header
        for row in csv_data:
            if row[0] == 'F':
                female_data.append([float(row[1]),float(row[2])])
            elif row[0] == 'M':
                male_data.append([float(row[1]),float(row[2])])

    return female_data, male_data

def histogram_plot(x,y,x_label,y_label,file_name):
    counts_x, bin_edges_x = np.histogram(x, bins=50)
    counts_y, bin_edges_y = np.histogram(y, bins=50)
    column_width = np.min(bin_edges_x[1:] - bin_edges_x[:-1])
    plt.bar(0.5*(bin_edges_x[1:] +bin_edges_x[:-1]),  counts_x, label=x_label, alpha=0.5, width=column_width)
    plt.bar(0.5*(bin_edges_y[1:] +bin_edges_y[:-1]),  counts_y, label=y_label, alpha=0.5, width=column_width)
    plt.legend(loc=0)
    plt.savefig(file_name)
    plt.close()

main()
