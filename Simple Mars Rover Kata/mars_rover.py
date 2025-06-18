class MarsRover:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'N'
        self.turn_left_map = {
            'N': 'W',
            'W': 'S',
            'S': 'E',
            'E': 'N'
        }
        self.turn_right_map = {
            'N': 'E',
            'E': 'S',
            'S': 'W',
            'W': 'N'
        }
        self.move_deltas = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }
    def execute(self, command_string: str) -> str:
        for command in command_string:
            if command == "L":
                self.direction = self.turn_left_map[self.direction]
            elif command == "R":
                self.direction = self.turn_right_map[self.direction]
            elif command == "M":
                delta_x, delta_y = self.move_deltas[self.direction]
                self.x = (self.x + delta_x) % 10
                self.y = (self.y + delta_y) % 10
        return f"{self.x}:{self.y}:{self.direction}"


