import csv
import os


class Validation:
    def __init__(self, valid_fieldnames):
        self.valid_fieldnames = valid_fieldnames
        self.csv_files = []
        self.valid_csv_files = []

    def detect_csv_files(self):
        for files in os.listdir(os.path.dirname(__file__)):
            if files.endswith('.csv'):
                self.csv_files.append(files)

    def validate_fieldnames(self):
        for i in range(len(self.csv_files)):
            with open(self.csv_files[i]) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                if self.valid_fieldnames == csv_reader.fieldnames:
                    self.valid_csv_files.append(self.csv_files[i])

