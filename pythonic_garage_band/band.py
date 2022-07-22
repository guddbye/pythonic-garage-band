class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)


class Musician:
    pass


class Guitarist:
    pass


class Bassist:
    pass


class Drummer:
    pass