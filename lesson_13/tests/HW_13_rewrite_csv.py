import csv
from pathlib import Path

file_name1 = "random.csv"
file_name2 = "rmc.csv"


def rewrite_unique_csv(file_name):

    data_path_file = Path('../data') / file_name
    data_path_file = data_path_file.absolute()
    data_path_file_uniq = Path('../data/feshchenko_uniq_' + file_name)
    data_path_file_uniq = data_path_file_uniq.absolute()

    with open(data_path_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        unique_rows = set(tuple(row) for row in reader)

    with open(data_path_file_uniq, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(unique_rows)



rewrite_unique_csv(file_name1)
rewrite_unique_csv(file_name2)
