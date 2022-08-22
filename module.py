class dog(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = int(weight)

    def weight_in_lb(self):
        return self.weight / 20


dog1 = dog("d1", 30)
print(dog1.weight_in_lb())
