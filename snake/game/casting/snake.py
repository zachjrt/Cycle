import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._tail_color = 0 # constants.GREEN
        # self.prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
        if self._segments[i].get_color() != constants.WHITE:
            self.grow_tail(1)
    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._tail_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def prepare_body(self, player):
        x_pos = 1 if player == "s1" else 3
        self._tail_color = constants.GREEN if player == "s1" else constants.RED

        # x = int(constants.MAX_X / x_pos)
        # y = int(constants.MAX_Y / x_pos)
        x= 150 * x_pos
        y = 150 * x_pos

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else self._tail_color
            
            segment = Actor()
            segment.set_position(position)   # 
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)