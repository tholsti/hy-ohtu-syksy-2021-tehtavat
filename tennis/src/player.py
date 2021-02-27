class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        pass

    def get_name(self):
        return self.name
    
    def get_points(self):
        return self.points
    
    def set_points(self, points):
        self.points = points

    def add_point(self):
        self.points += 1
