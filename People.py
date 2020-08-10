class people:

    def __init__(self, name):
        self.name = name
        self.purchase_descrip = []
        self.purchase_price_descrip = []
        self.purchases = []
        self.total_spent = 0
        self.debt = 0
        self.debt_temp = 0
        self.pay = []
        self.pay_out = []
        self.pay_who = []

    def add_purchase(self, purchase):
        self.purchases.append(purchase)

    def add_description(self, description):
        self.purchase_descrip.append(description)

    def get_purchase(self):
        return self.purchases

    def get_description(self):
        return self.purchase_descrip

    def set_total(self):
        self.total_spent = 0
        for items in self.purchases:
            self.total_spent = self.total_spent+float(items)

    def get_total(self):
        return self.total_spent

    def get_name(self):
        return self.name

    def add_purchase_descrip(self, price, description):
        self.purchase_price_descrip.append("$"+str(price)+"   "+description)

    def get_purchase_descrip(self):
        return self.purchase_price_descrip

    def set_debt(self, cost_per_person):
        self.debt = float(self.total_spent)-cost_per_person

    def get_debt(self):
        return self.debt

    def add_payment(self, payment):
        self.pay.append(payment)

    def get_pay(self):
        return self.pay

    def add_pay_who(self, who_to_pay):
        self.pay_who.append(who_to_pay)

    def get_pay_who(self):
        return self.pay_who

    def set_debt_temp(self):
        self.debt_temp = self.debt

    def get_temp_debt(self):
        return self.debt_temp

    def update_temp_debt(self, payment):
        self.debt_temp = self.debt_temp+payment*-1

    def pay_temp_debt(self, payment):
        self.debt_temp-payment

    def round_payments(self):
        for x in range(0, len(self.pay)):
            self.pay[x] = round(self.pay[x], 2)

    def round_purchases(self):
        for x in range(0, len(self.purchases)):
            self.purchases[x] = round(float(self.purchases[x]), 2)



