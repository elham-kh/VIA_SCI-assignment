from utils import *

# read csv file and extract data for female and male
female_data, male_data = csv_reader('../data/data.csv')

# plot age data
histogram_plot([row[0] for row in female_data],[row[0] for row in male_data],'women\'s age','men\'s age','age.png','Histogram for Women\'s and Men\'s Age ','Age')

# plot height data
histogram_plot([row[1] for row in female_data],[row[1] for row in male_data],'women\'s height','men\'s height','height.png','Histogram for Women\'s and Men\'s Height ','Height')
