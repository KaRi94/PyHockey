__author__ = 'Asia'


class WrongTypeException(Exception):
    """
    raised when the parameter is wrong type
    """
    pass


class OutOfRangeException(Exception):
    """
    raised when the disk is out of the pitch
    """
    pass


class Goal:
    """
    class represent a goal on the Pitch
    """
    def __init__(self, x, y_center, width):
        """
        define constructor of class Goal. If the value will not be equal 'L' or 'R', the function raise the ValueError
        :param x: x position
        :param y_center: y coordinate of the center of goal
        :param width: width of goal which is measured along y axis.
        :param goal_type: 'l' for left and 'r' for right goal
        :return: none
        :raise: WrongTypeException if v is not type of int
        """
        self.j_min = y_center - 0.5 * width
        self.j_max = y_center + 0.5 * width
        self.i = x

    def in_goal(self, i, j, r):
        """
        :param i: x coordinates of disk
        :param j: y coordinates of disk
        :param r: radius of disk
        :raise: WrongTypeException if i, j or r is not type of int, OutOfRangeException if disk is out of pitch
        """
        if abs(i - self.i) < r and self.j_min < j < self.j_max:
            return True
        else:
            return False

