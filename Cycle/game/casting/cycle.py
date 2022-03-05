import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A light cycle that leaves behind a trail that is akin to a wall
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of victories.
    """
    def __init__(self):
        """Consructs a cycle
        """
        super().__init__()
        self._segments = []
        self._trail_color = 0 # constants.GREEN
        # self.prepare_body()

    def get_segments(self):
        """Returns the segments of the light trail
        
        """
        return self._segments

    def move_next(self):
        """moves the cycle and each of it's segments forward
        
        """
        for segment in self._segments:
            segment.move_next()
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
        if self._segments[i].get_color() != constants.WHITE:
            self.grow_trail(1)

    def get_body(self):
        """Returns the front of the cycle
        """
        return self._segments[0]

    def grow_trail(self, number_of_segments):
        """expands the light trail
        
        Args:
            number of segments (int): number of segments in the cycle
        """
        for i in range(number_of_segments):
            trail = self._segments[-1]
            velocity = trail.get_velocity()
            offset = velocity.reverse()
            position = trail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._trail_color)
            self._segments.append(segment)

    def turn_body(self, velocity):
        """Turns the front of the cycle
        
        Args:
            velocity (int): speed cycle is moving at
        """
        self._segments[0].set_velocity(velocity)
    
    def prepare_body(self, player):
        """Prepares the cycle and it's trail
        
        Args:
            player (object): the player
        """
        x_pos = 1 if player == "c1" else 3
        self._trail_color = constants.GREEN if player == "c1" else constants.RED

        # x = int(constants.MAX_X / x_pos)
        # y = int(constants.MAX_Y / x_pos)
        x= 150 * x_pos
        y = 150 * x_pos

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else self._trail_color
            
            segment = Actor()
            segment.set_position(position)   # 
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)