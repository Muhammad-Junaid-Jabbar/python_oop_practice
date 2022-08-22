class employee:
    raise_amount = 1.00

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    def __repr__(self):
        return "employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)


jim = employee("Jim", "Smith", 50000)
employee.set_raise_amt(1.05)
kim = employee("kim", "jones", 60000)
kim.apply_raise()
print(jim.__repr__())
print(kim.__repr__())
