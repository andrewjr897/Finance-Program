
class bank:

    def __init__(self):
        self.trip_name = ""
        self.trip_month = ""
        self.trip_year = ""
        self.total_spent = 0
        self.individual_debt = 0

    def set_trip_name(self, name):
        self.trip_name = name

    def set_trip_date(self, month, year):
        self.trip_month = month
        self.trip_year = year

    def get_trip_name(self):
        return self.trip_name

    def get_trip_month(self):
        return self.trip_month

    def get_trip_year(self):
        return self.trip_year

    def add_total_spent(self, purchase):
        self.total_spent = self.total_spent+float(purchase)

    def get_total_spent(self):
        return self.total_spent

    def set_individual_debt(self, numpeople):
        self.individual_debt = self.total_spent/numpeople

    def get_individual_debt(self):
        return self.individual_debt

