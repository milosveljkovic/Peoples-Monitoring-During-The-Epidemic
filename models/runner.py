class Runner:

    def __init__(self, name, device, initial_x_coordinate, initial_y_coordinate, activity_level, goal_distance):
        self.name = name
        self.device = device
        self.initial_x_coordinate = initial_x_coordinate
        self.initial_y_coordinate = initial_y_coordinate
        self.activity_level = activity_level
        self.goal_distance = goal_distance

    def get_coordinates(self):
        return {'x': self.initial_x_coordinate,
                'y': self.initial_y_coordinate}

    def set_coordinates(self, x, y):
        self.initial_x_coordinate = x
        self.initial_y_coordinate = y
