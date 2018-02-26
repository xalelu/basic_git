class One():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age


class two():
    def __init__(self):
        self.name = 'two'


class three():
    def __init__(self, name, descript):
        self.name = name
        self.descript = descript

class four():
    def __init__(self, name, tagname):
        self.name = name
        self.tagname = tagname


if __name__ == '__main__':
    two = two()
    three = three('tina', 'that my helf.')
    four = four('four_one', 'four_two')
    print(three.name)