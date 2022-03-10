import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.cast import Cast


class ControlActorsAction(Action):
    """
    An input action that controls the cycles and keeping scores for both snakes (cyles)
    
    The responsibility of ControlActorsAction is to get the direction and move the cycles forward.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(constants.CELL_SIZE, 0)
        
    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        score = cast.get_first_actor("scores")
        score2 = cast.get_first_actor("scores2")

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            score.add_points(100)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            score.add_points(100)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            score.add_points(100)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            score.add_points(100)
        
        cycle = cast.get_first_actor("cycles")
        cycle.turn_body(self._direction)

        # move snake 2 and add score to snake 2

        if self._keyboard_service.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)
            score2.add_points(100)

        if  self._keyboard_service.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE, 0)
            score2.add_points(100)

        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)
            score2.add_points(100)

        if  self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)
            score2.add_points(100)
        
        cycle2 = cast.get_first_actor("cycles2")
        cycle2.turn_body(self._direction2)
