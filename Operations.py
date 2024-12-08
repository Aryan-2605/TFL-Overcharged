from OpenFiles import OpenFiles
class Operations:
    def __init__(self, headers, description):
        self.index = []
        self.headers = headers
        self.description = description
        self.TFL_charges = {}

    def tfl_charges_indexed(self):
        for i, date in enumerate(self.headers['Description']):
            if self.headers['Description'][i] == self.description:
                self.index.append(i)


    def merge_dates(self):
        for i in self.index:
            date = self.headers['Date'][i]
            cost = float(self.headers['Amount'][i])

            if date in self.TFL_charges:
                self.TFL_charges[date] += cost
            else:
                self.TFL_charges[date] = cost



    def format_row(self):
        total_cost = 0
        for date, total in self.TFL_charges.items():
            OpenFiles.export_row(date, self.description, round(total,2))
            total_cost += total
