import csv
import os


class OpenFiles:

    @staticmethod
    def open_file(filenames):
        with open(filenames, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)

            file = {header: [] for header in reader.fieldnames}

            for row in reader:
                for header, value in row.items():
                    file[header].append(value)

        return file

    @staticmethod
    def export_row(date, description, amount):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, 'Output')
        output_file = os.path.join(output_dir, 'TFL Output.csv')
        with open(output_file, mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([date, description, amount])

    @staticmethod
    def wipe_file():
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, 'Output')
        output_file = os.path.join(output_dir, 'TFL Output.csv')
        with open(output_file, mode='w', newline='') as csvfile:
            pass
