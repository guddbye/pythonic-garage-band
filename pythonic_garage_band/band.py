class Band:

    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)


class Musician:
    def __init__(self, name):
        self.name = name

class Guitarist:
    pass


class Bassist:
    pass


class Drummer:
    pass