from Validation import Validation
from OpenFiles import OpenFiles
from Operations import Operations


class Application:
    def __init__(self, charge_description, field_names):
        self.charge_description = charge_description
        self.fieldnames = field_names

    def run(self):
        OpenFiles.wipe_file()

        all_files = Validation(self.fieldnames)
        all_files.detect_csv_files()
        all_files.validate_fieldnames()
        cleaned_files = all_files.valid_csv_files

        print(all_files.csv_files)
        print(all_files.valid_csv_files)
        #print(OpenFiles.open_file('activity.csv'))
        for name in cleaned_files:
            numerations = Operations(OpenFiles.open_file(name), charge_description)
            numerations.tfl_charges_indexed()
            numerations.merge_dates()
            numerations.format_row()







if __name__ == '__main__':
    charge_description = 'TFL TRAVEL CHARGE       TFL.GOV.UK/CP'
    field_names = ['Date', 'Description', 'Amount']
    app = Application(charge_description, field_names)
    app.run()
