import numpy as np
import matplotlib.pyplot as plt
import csv
from os import path



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

# function to plot the data in histogram form
def histogram_plot(x,y,x_label,y_label,file_name):
    counts_x, bin_edges_x, counts_y, bin_edges_y, column_width = calculate_histogram(x,y)
    plt.bar(0.5*(bin_edges_x[1:] +bin_edges_x[:-1]),  counts_x, label=x_label, alpha=0.5, width=column_width)
    plt.bar(0.5*(bin_edges_y[1:] +bin_edges_y[:-1]),  counts_y, label=y_label, alpha=0.5, width=column_width)
    plt.legend(loc=0)
    file_path = path.join('results', file_name)
    plt.savefig(file_path)
    plt.close()

# function to generate histogram
def calculate_histogram(x,y):
    counts_x, bin_edges_x = np.histogram(x, bins=50)
    counts_y, bin_edges_y = np.histogram(y, bins=50)
    column_width = np.min(bin_edges_x[1:] - bin_edges_x[:-1])
    return  counts_x, bin_edges_x, counts_y, bin_edges_y, column_width
